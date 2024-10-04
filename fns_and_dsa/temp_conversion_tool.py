FAHRENHEIT_TO_CELSIUS_FACTOR= 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR= 9/5

def convert_to_celsius(fahrenheit):

    return (fahrenheit -32)* FAHRENHEIT_TO_CELSIUS_FACTOR
    

def convert_to_fahrenheit(celsius):

    return (celsius* CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


temperatur = float(input("Enter the temperature to convert:"))

unit = (input("Is this temperature in Celsius or Fahrenheit? (C/F):"))

if unit == "f":

 print (f"{temperatur}°C is {str (convert_to_celsius(temperatur))}°F")

elif unit == "c":
   print (f"{temperatur}°F is {str (convert_to_fahrenheit(temperatur))}°C")

else :
   
   raise ValueError("Invalid temperature. Please enter a numeric value.")