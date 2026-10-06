# Task 9: Simple Interest
# Accept principal, rate, and time and calculate simple interest and total amount.

principal = float(input("Enter Principal Amount :- "))
rate = int(input("Enter rate of Interest :- "))
time = int(input("Enter time (In years) :- "))

# interest = principal * (rate / 100) * time
interest = (principal * rate  * time)/ 100

total_amount = principal + interest

print("Interest :- ",interest)
print("Total Amount :- ",total_amount)