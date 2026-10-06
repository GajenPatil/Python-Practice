# Task 2: Personal Information
# Create variables for a person's name, age, email, mobile number, city, and profession. Display a formatted profile.

name = input("Enter your name : ")
age = int(input("Enter Your Age : "))
email = input("Enter your Email Id : ")
m_no = int(input("Enter your Contact Number : "))
city = input("Enter your City : ")
profession = input("Enter Profession : ")


print("Information Recorded...!!!!")
print("Your name is ",name)
print(f"Your are {age} years old.")
print(f"Your Email  ID is {email}")
print(f"You live in {city}.")
print(f"Your Contact number is {m_no}")
print(f"Your are a {profession}")