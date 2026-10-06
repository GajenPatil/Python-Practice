# Task 3: Simple Calculator
# Accept two numbers and display addition, subtraction, multiplication, division, floor division, modulus, and power.

num1 = float(input("Enter 1st Number : "))
oprt = input("Enter operator : ")
num2 = float(input("Enter 2nd Number : "))

match oprt:
    case "+" :
        res = num1 + num2
        print(f"{num1} + {num2} = {res}")
    case "-":
        res = num1 - num2
        print(f"{num1} - {num2} = {res}")
    case "*":
        res = num1 - num2
        print(f"{num1} * {num2} = {res}")
    case "/":
        res = num1 / num2
        print(f"{num1} / {num2} = {res}")
    case "%":
        res = num1 % num2
        print(f"{num1} % {num2} = {res}")
    case "//":
        res = num1 // num2
        print(f"{num1} // {num2} = {res}")
    case "**":
        res = num1 ** num2
        print(f"{num1} ** {num2} = {res}")
    case _ :
        print("Invalid Operator :)")