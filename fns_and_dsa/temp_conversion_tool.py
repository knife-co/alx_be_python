FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temperature_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}\u00B0C is {fahrenheit}\u00B0F")

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}\u00B0F is {celsius}\u00B0C")

if temperature_unit == "C":
    celsius = int(input("Enter the temperature to convert: "))
    convert_to_fahrenheit(celsius)
elif temperature_unit == "F":
    fahrenheit = int(input("Enter the temperature to convert: "))
    convert_to_celsius(fahrenheit)
else:
    print ("Invalid temperature. Please enter a numeric value.")
        