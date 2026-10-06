# Task 4: Area and Perimeter
# Accept rectangle dimensions and calculate area and perimeter.

print("Emter Values in Meter ")
length = float(input("Enter Length of Rectangle :- "))
breadth = float(input("Enter Breadth of Rectangle :- "))

perimeter = 2 * (breadth + length) 
area = length * breadth

print(f"Perimeter of rectangle is {perimeter}m.")
print(f"Area of rectangle is {area}sq.m")