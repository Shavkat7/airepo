def convert_cel_to_far():
    Celsius_degrees = float(input("Enter a temperature in degrees C:"))
    Farenheit_degrees = Celsius_degrees * 9/5 + 32
    return f"{Celsius_degrees} degrees C = {Farenheit_degrees:.2f} degrees F"

def convert_far_to_cel():
    Farenheit_degrees = float(input("Enter a temperature in degrees F:"))
    Celsius_degrees = (Farenheit_degrees - 32) * 5/9
    return f"{Farenheit_degrees} degrees F = {Celsius_degrees:.2f} degrees C"

print(convert_far_to_cel())
print(convert_cel_to_far())
