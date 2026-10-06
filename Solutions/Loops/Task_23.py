# Task 23: Multiplication Table
# Print the multiplication table of a number up to 20.

number = int(input("Enter Number :- "))

# using while loop

count = 0

while count < 20 :
    count += 1

    mul = count*number
    print(mul)


# using for loop

# for i in range(1,21):
#     mul = i * number
#     print(mul)