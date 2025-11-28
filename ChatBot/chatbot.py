print ("Hello! My name is Emi"
       "\nI was created in 2025")


print ("Please, remind me your name.")
your_name = input()
print(f"What a great name you have, {your_name}")


print("Let me guess your age."
      "\nEnter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {age}; that's a good time to start programming!")


print("Now I will prove to you that I can count to any number you want.")
number_to_count = int(input())
i = 0
while i <= number_to_count:
    print(f"{i}!")
    i += 1
print("Completed, have a nice day!")


print("Let's test your programming knowledge!"
      "\nWhy do we use methods?"
      "\n1. To repeat a statement multiple times."
      "\n2. To decompose a program into several small subroutines."
      "\n3. To determine the execution time of a program."
      "\n4. To interrupt the execution of a program.")
while True:
    answer = int(input())
    if answer == 2:
        print ("Completed, have a nice day!")
        break
    else:
        print("Please, try again.")
print("Congratulations, have a nice day!")

