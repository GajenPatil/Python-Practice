# Task 13: Largest of Two
# Find the larger of two numbers without using max().

num1 = int(input("Enter Number :- "))
num2 = int(input("Enter Number :- "))

if num1 > num2 :
    print(f"{num1} is Greater than {num2}.")
elif num2 > num1:
    print(f"{num2} is Greater than {num1}.")
else :
    print("Both Numbers are Equal.")