import random
def dinner():
    """
    Description:
    Collects names of participants and a total bill amount.
    Calculates the share for each person, optionally excluding one
    randomly chosen "lucky" person from the payment.

    Parameters:
    (No parameters)

    Returns:
    None: Results are printed as a dictionary to the console.
    """
    print("Enter the number of friends joining (including you):")
    input_value = input("> ")


    if not input_value.isdigit() or int(input_value) <= 0:
        print("\nNo one is joining for the party")
    else:
        num_people = int(input_value)
        friends_dict = {}


        print("\nEnter the name of every friend (including you), each on a new line:")
        for _ in range(num_people):
            name = input("> ")
            friends_dict[name] = 0


        print("\nEnter the total amount:")
        total_bill = float(input("> "))


        print("\nDo you want to use the \"Who is lucky?\" feature? Write Yes/No:")
        lucky_choice = input("> ")

        lucky_one = None
        if lucky_choice == "Yes":
            lucky_one = random.choice(list(friends_dict.keys()))
            print(f"\n{lucky_one} is the lucky one!")
        else:
            print("\nNo one is going to be lucky")


        if lucky_one:
            split_value = round(total_bill / (num_people - 1), 2)
            for friend in friends_dict:
                friends_dict[friend] = split_value
            friends_dict[lucky_one] = 0
        else:
            split_value = round(total_bill / num_people, 2)
            for friend in friends_dict:
                friends_dict[friend] = split_value
        print(f"\n{friends_dict}")

if __name__ == "__main__":
    dinner()