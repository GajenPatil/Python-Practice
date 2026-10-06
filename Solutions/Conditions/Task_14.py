# Task 14: Largest of Three
# Find the largest of three numbers using conditional statements


num1 = int(input("Enter Number :- "))
num2 = int(input("Enter Number :- "))
num3 = int(input("Enter Number :- "))


if num1 > num2:
    if num1 > num3:
        print(f"{num1} is Greater than {num2} and {num3}.")
    elif num1 == num2 == num3 :
        print("All numbers are equal.")
    else:
        print(f"{num3} is Greater than {num1} and {num2}.")
else :
    if num2 > num3:
        print(f"{num2} is Greater than {num1} and {num3}.")
    elif num1 == num2 == num3 :
        print("All numbers are equal.")
    else:
        print(f"{num3} is Greater than {num1} and {num2}.")