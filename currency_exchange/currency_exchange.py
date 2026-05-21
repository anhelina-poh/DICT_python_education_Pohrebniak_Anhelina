import json
import urllib.request
import urllib.error
from typing import Dict


class NegativeAmountError(Exception):
    """Raised when the user enters a negative monetary amount."""
    pass


class CurrencyNotFoundError(Exception):
    """Raised when the target currency code does not exist in the API data."""
    pass


class NetworkError(Exception):
    """Raised during connectivity issues or JSON parsing failures."""
    pass


class EmptyInputError(Exception):
    """Raised when mandatory input is left blank."""
    pass


class CurrencyExchangeApp:
    """
    Description:
    A currency conversion tool that fetches live exchange rates from
    FloatRates.com. It uses a local dictionary as a cache to store
    previously requested rates, reducing API dependency.

    Parameters:
    (No parameters for initialization)

    Returns:
    None: Outputs conversion results directly to the console.
    """

    def __init__(self) -> None:
        self.cache: Dict[str, float] = {}
        self.base_currency: str = ""

    def fetch_all_rates(self) -> Dict[str, dict]:
        """
        Fetches all current exchange rates for the base currency using urllib.
        """
        url = f"https://www.floatrates.com/daily/{self.base_currency}.json"
        try:
            with urllib.request.urlopen(url) as response:
                if response.status != 200:
                    raise NetworkError(f"HTTP status: {response.status}")
                return json.loads(response.read().decode('utf-8'))
        except urllib.error.URLError as e:
            raise NetworkError(f"Network error: {e.reason}")
        except json.JSONDecodeError as e:
            raise NetworkError(f"JSON decoding error: {e}")

    def run(self) -> None:
        """The main execution loop for the exchange application."""


        try:
            user_input = input().strip()
            if not user_input:
                return
            self.base_currency = user_input.lower()
        except EOFError:
            return


        try:
            rates = self.fetch_all_rates()
            if self.base_currency != "usd" and "usd" in rates:
                self.cache["usd"] = rates["usd"]["rate"]
            if self.base_currency != "eur" and "eur" in rates:
                self.cache["eur"] = rates["eur"]["rate"]
        except NetworkError:
            pass


        while True:
            try:
                target_currency = input().strip().lower()
                if not target_currency:
                    break

                amount_str = input().strip()
                if not amount_str:
                    break

                amount = float(amount_str)
                if amount < 0:
                    raise NegativeAmountError("The amount cannot be negative")
            except (EOFError, ValueError, NegativeAmountError):
                break

            print("Checking the cache...")

            if target_currency in self.cache:
                print("It is in the cache!")
                rate = self.cache[target_currency]
            else:
                print("Sorry, but it is not in the cache!")
                try:
                    fresh_rates = self.fetch_all_rates()
                    if target_currency in fresh_rates:
                        rate = fresh_rates[target_currency]["rate"]
                        self.cache[target_currency] = rate
                    else:
                        raise CurrencyNotFoundError(f"Rate for {target_currency} not found")
                except (NetworkError, CurrencyNotFoundError):
                    print("Unknown currency or network error.")
                    continue

            result = round(amount * rate, 2)
            print(f"You received {result} {target_currency.upper()}.")


if __name__ == "__main__":
    app = CurrencyExchangeApp()
    app.run()