# Task 8: Currency Breakdown
# Accept an amount and determine the number of notes required for selected denominations.

amount = int(input("Enter Amount :- "))

note_500 = amount // 500
remaining1 = amount % 500

note_200 = remaining1 // 200
remaining2 = remaining1 % 200

note_100 = remaining2 // 100
remaining3 = remaining2 % 100

note_50 = remaining3 // 50
remaining4 = remaining3 % 50

note_20 = remaining4 // 20
remaining5 = remaining4 % 20

note_10 = remaining5 // 10
remaining6 = remaining5 % 10

coin_5 = remaining6 // 5
remaining7 = remaining6 % 5

coin_2 = remaining7 // 2
remaining8 = remaining7 % 2

coin_1 = remaining8 


print("500 Rs. notes :- ",note_500)
print("200 Rs. notes :- ",note_200)
print("100 Rs. notes :- ",note_100)
print("50 Rs. notes :- ",note_50)
print("20 Rs. notes :- ",note_20)
print("10 Rs. notes :- ",note_10)
print("5 Rs. notes :- ",coin_5)
print("2 Rs. notes :- ",coin_2)
print("1 Rs. notes :- ",coin_1)