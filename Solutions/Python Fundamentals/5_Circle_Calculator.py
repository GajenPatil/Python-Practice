# Task 5: Circle Calculator
# Accept radius and calculate area and circumference using a constant for pi.

pi = 22/7

radius = float(input("Enter radius of Circle :- "))

area = pi*(radius**2)
circumference = 2 * pi * radius

print(f"Area of Circle is {area} sq.")
print(f"Circumference of Circle is {circumference} ")
