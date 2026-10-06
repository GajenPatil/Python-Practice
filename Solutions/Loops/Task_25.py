# Task 25: Factorial
# Calculate factorial without using math.factorial().

number = int(input("Enter number :- "))

# using while loop

count = 0
factorial = 1

while count < number :
    count += 1
    factorial  = factorial * count

print(f"factorial 0f {number} is {factorial}")

# using while loop

# factorial = 1

# for i in range(1,number+1):
#     factorial = factorial * i

# print(f"factorial 0f {number} is {factorial}")
