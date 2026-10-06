# Task 10: Salary Calculator
# Accept basic salary, allowance percentage, and deduction percentage and calculate net salary.

basic_salary = float(input("Enter Basic Salary :- "))

allowance = basic_salary*0.25

deduction = basic_salary*0.18

net_salary = basic_salary + allowance - deduction

print("-------------------------------------------")
print("Salary Details")
print("-------------------------------------------")
print("Basic Salary :- ",basic_salary)
print("Allowance :- ",allowance)
print("Deduction :- ",deduction)
print("Net Salary :- ",net_salary)