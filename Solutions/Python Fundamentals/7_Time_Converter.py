# Task 7: Time Converter
# Convert a number of seconds into hours, minutes, and remaining seconds.

input_sec = int(input("Enter seconds for conversion :- "))

hours = input_sec // 3600
minutes = (input_sec % 3600)//60
seconds = (input_sec % 3600) % 60

print(f"Time format HH:MM:SS {hours}:{minutes}:{seconds}")
