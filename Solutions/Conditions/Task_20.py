# Task 20: Triangle Validator
# Validate three sides and classify a valid triangle as equilateral, isosceles, or scalene.

side1 = float(input("Enter 1st side length :- "))
side2 = float(input("Enter 2nd side length :- "))
side3 = float(input("Enter 3rd side length :- "))

if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1) :
    if side1 == side2 and side2 == side3 :
        print("This Triangle is Equilateral.")
    elif side1 == side2 or side2 == side3 or side3 == side1 :
        print("This Triangle is Isosceles.")
    else :
        print("This triangle is Scalene.")
else :
    print("This is not valid Triangle.")