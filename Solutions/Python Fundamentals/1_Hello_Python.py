# Task 1: Hello Python
# Write a program that displays your name, age, city, and a short introduction. Store each value in a variable.

name = input("Enter your name : ")
age = int(input("Enter Your Age : "))
city = input("Enter your City : ")
intro = input("Introduce Yourself : ")

print("Information Recorded...!!!!")
print("Your name is ",name)
print(f"Your are {age} years old.")
print(f"You live in {city}.")
print(f"Your Introduction :- {intro}")