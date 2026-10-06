# Task 6: Temperature Converter
# Convert Celsius to Fahrenheit and Kelvin.

celsius = float(input("Enter Temperature in Celsius :- "))

fahrenheit = (celsius*(9/5))+32
kelvin = celsius + 273.15

print(f"{celsius} convert into {fahrenheit} fehrenheit.")
print(f"{kelvin} convert into {kelvin} kelvin.")