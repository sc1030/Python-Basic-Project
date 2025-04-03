'''temp = float(input("Enter Temperature: "))
unit = input("Convert To (f)ahrenheit or (C)elsius ").upper()

if unit == 'F':
    print(f"{temp}°C is {(temp * 9/5) + 32}°F")
elif unit == "C":
    print(f"{temp}°F is {(temp - 32) * 5/9}°C")
else:
    print("Invalid unit! Exiting")
    '''
    
def convert_temperature():
    """
    Convert temperature between Celsius and Fahrenheit with robust validation and user-friendly interaction.
    """
    while True:
        try:
            temp = float(input("Enter temperature: ").strip())
            break
        except ValueError:
            print("Invalid input! Please enter a valid numeric temperature.")
    
    while True:
        unit = input("Convert to (F)ahrenheit or (C)elsius? ").strip().upper()
        if unit in ("F", "C"):
            break
        print("Invalid unit! Please enter 'F' or 'C'.")
    
    converted_temp = (temp * 9/5 + 32) if unit == "F" else (temp - 32) * 5/9
    original_unit = "°C" if unit == "F" else "°F"
    target_unit = "°F" if unit == "F" else "°C"
    print(f"{temp}{original_unit} is {converted_temp:.2f}{target_unit}")
    
    # Logging conversion history (optional feature)
    with open("temperature_conversion_log.txt", "a") as log_file:
        log_file.write(f"{temp}{original_unit} -> {converted_temp:.2f}{target_unit}\n")

if __name__ == "__main__":
    convert_temperature()

    