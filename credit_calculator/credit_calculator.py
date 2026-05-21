import argparse
import math
import sys
from typing import List, Union


class InvalidParametersError(Exception):
    """Raised when command-line arguments are logically invalid."""
    pass


class CalculationError(Exception):
    """Raised when calculation fails due to invalid mathematical input values."""
    pass


class CreditCalculator:
    """
    Description:
    A command-line tool to calculate loan parameters. Supports 'annuity'
    (fixed payments) and 'diff' (differentiated) payment types. It can
    solve for missing variables like principal, monthly payment, or
    the number of periods required.

    Parameters:
    (Managed via command-line arguments: --type, --principal, --payment, --periods, --interest)

    Returns:
    None: Outputs results and overpayment calculations to the console.
    """

    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(description="Credit Calculator", add_help=False)
        self.parser.add_argument("--type", type=str)
        self.parser.add_argument("--principal", type=float)
        self.parser.add_argument("--payment", type=float)
        self.parser.add_argument("--periods", type=int)
        self.parser.add_argument("--interest", type=float)

    def parse_and_validate(self) -> argparse.Namespace:
        """Parses and validates logic rules for the provided arguments."""
        args, _ = self.parser.parse_known_args()

        if args.type not in ["annuity", "diff"] or args.interest is None:
            raise InvalidParametersError("Incorrect parameters")

        if args.type == "diff" and args.payment is not None:
            raise InvalidParametersError("Incorrect parameters")

        numeric_args = ["principal", "payment", "periods", "interest"]
        for arg_name in numeric_args:
            value = getattr(args, arg_name)
            if value is not None and value <= 0:
                raise InvalidParametersError("Incorrect parameters")

        if args.type == "annuity":
            provided = sum(1 for a in ["principal", "payment", "periods"] if getattr(args, a) is not None)
            if provided != 2:
                raise InvalidParametersError("Incorrect parameters")

        if args.type == "diff":
            if args.principal is None or args.periods is None:
                raise InvalidParametersError("Incorrect parameters")

        return args

    @staticmethod
    def calculate_annuity_payment(principal: float, annual_rate: float, periods: int) -> int:
        """Calculates fixed monthly payment using the annuity formula."""
        i = annual_rate / 100 / 12
        if i == 0:
            return math.ceil(principal / periods)

        power = math.pow(1 + i, periods)
        denominator = power - 1
        if denominator <= 0:
            raise CalculationError("Invalid parameters: denominator non-positive.")
        payment = principal * i * power / denominator
        return math.ceil(payment)

    @staticmethod
    def calculate_annuity_periods(principal: float, payment: float, annual_rate: float) -> int:
        """Calculates the number of months needed to repay the loan."""
        i = annual_rate / 100 / 12
        if i == 0:
            return math.ceil(principal / payment)

        if payment <= i * principal:
            raise CalculationError("Monthly payment is too low to cover interest.")

        argument = payment / (payment - i * principal)
        try:
            months = math.log(argument, 1 + i)
        except ValueError:
            raise CalculationError("Logarithm calculation failed.")
        return math.ceil(months)

    @staticmethod
    def calculate_annuity_principal(payment: float, annual_rate: float, periods: int) -> int:
        """Calculates the initial loan principal based on annuity payments."""
        i = annual_rate / 100 / 12
        if i == 0:
            return round(payment * periods)

        power = math.pow(1 + i, periods)
        denominator = power - 1
        if denominator <= 0:
            raise CalculationError("Invalid parameters: denominator non-positive.")
        annuity_factor = i * power / denominator
        principal = payment / annuity_factor
        return round(principal)

    @staticmethod
    def calculate_diff_payments(principal: float, annual_rate: float, periods: int) -> List[int]:
        """Calculates a list of monthly payments for a differentiated loan."""
        i = annual_rate / 100 / 12
        monthly_principal = principal / periods
        payments = []
        for m in range(1, periods + 1):
            remain = principal - monthly_principal * (m - 1)
            payment = monthly_principal + i * remain
            payments.append(math.ceil(payment))
        return payments

    @staticmethod
    def format_periods(months: int) -> str:
        """Converts raw months into a human-readable 'Years and Months' format."""
        years = months // 12
        remain_months = months % 12

        if years == 0:
            return f"{remain_months} month{'s' if remain_months != 1 else ''}"
        elif remain_months == 0:
            return f"{years} year{'s' if years != 1 else ''}"
        else:
            return (f"{years} year{'s' if years != 1 else ''} and {remain_months} month"
                    f"{'s' if remain_months != 1 else ''}")

    @staticmethod
    def compute_overpay(total_paid: Union[float, int], principal: float) -> int:
        """Calculates the total interest paid over the life of the loan."""
        return round(total_paid - principal)

    def run(self) -> None:
        """Main execution logic routing to specific calculation types."""
        try:
            args = self.parse_and_validate()

            if args.type == "diff":
                payments = self.calculate_diff_payments(args.principal, args.interest, args.periods)
                for idx, payment in enumerate(payments, start=1):
                    print(f"Month {idx}: payment is {payment}")

                total_paid = sum(payments)
                overpayment = self.compute_overpay(total_paid, args.principal)
                print(f"\nOverpayment = {overpayment}")

            else:
                if args.principal is None:
                    principal = self.calculate_annuity_principal(args.payment, args.interest, args.periods)
                    total_paid = args.payment * args.periods
                    overpayment = self.compute_overpay(total_paid, principal)
                    print(f"Your loan principal = {principal}!")
                    print(f"Overpayment = {overpayment}")

                elif args.payment is None:
                    payment = self.calculate_annuity_payment(args.principal, args.interest, args.periods)
                    total_paid = payment * args.periods
                    overpayment = self.compute_overpay(total_paid, args.principal)
                    print(f"Your annuity payment = {payment}!")
                    print(f"Overpayment = {overpayment}")

                elif args.periods is None:
                    months = self.calculate_annuity_periods(args.principal, args.payment, args.interest)
                    total_paid = args.payment * months
                    overpayment = self.compute_overpay(total_paid, args.principal)
                    formatted_time = self.format_periods(months)
                    print(f"It will take {formatted_time} to repay this loan!")
                    print(f"Overpayment = {overpayment}")

        except (InvalidParametersError, CalculationError):
            print("Incorrect parameters")
            sys.exit(1)


if __name__ == "__main__":
    app = CreditCalculator()
    app.run()