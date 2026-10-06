# Task 19: Login Validation
# Create a simple username/password login with a limited number of attempts.


username = "gajen"
password = "gajen27"

setusername = input("Enter Username :- ")
setpassword = input("Enter Password :- ")

if password == setpassword :
    print("Welcome to profile......")
else :
    print("2 Attempt left")
    setusername = input("Enter Username :- ")
    setpassword = input("Enter Password :- ")

    if password == setpassword :
        print("Welcome to profile......")
    else :
        print("1 Attempt left")
        setusername = input("Enter Username :- ")
        setpassword = input("Enter Password :- ")

        if password == setpassword :
            print("Welcome to profile......")
        else :
            print("Your profile is Locked")
