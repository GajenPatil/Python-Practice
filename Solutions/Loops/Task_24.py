# Task 24: Sum of Natural Numbers
# Calculate the sum from 1 to N using a loop.

number = int(input("Enter number :- "))

# using while loop

count = 0
sum = 0

while count < number :
    count += 1
    sum  = sum + count
print(sum)

# using while loop

# sum = 0

# for i in range(1,number+1):
#     sum = sum + i

# print(f"Sum of numbers from 1 to {number} is {sum}")