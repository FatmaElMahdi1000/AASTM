def converter(temp, temp_type):
    while True:
        if temp == 0:
            print("Re-Enter Temp! INVALID VALUE")
            temp = int(input("Enter temperature: "))
            temp_type = input("Enter C or F: ").upper()
        elif isinstance(temp, int) and temp_type == "C":
            fahrenheit = (temp * 9/5) + 32
            return f"To Fahrenheit: {fahrenheit} °F"
        elif isinstance(temp, int) and temp_type == "F":
            celsius = (temp - 32) * 5/9
            return f"To Celsius: {celsius} °C"

temperature = int(input("Enter temperature: "))
temperature_type = input("Enter C or F: ").upper()
print(converter(temperature, temperature_type))
