# Task 15: Leap Year
# Determine whether a year is a leap year.

year = int(input("Enter Year here :- "))

if year % 4 == 0 :
    print(f"{year} is Leap year.")
else :
    print(f"{year} is not a Leap year.")


#Advance Version

# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print(f"{year} is a Leap year.")
# else:
#     print(f"{year} is not a Leap year.")