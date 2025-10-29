num = int(input("Enter a number: "))
if num < 1:
    abs_value = num * -1
    print(f"The absolute value of {num} is {abs_value}")
else:
    print(f"The absolute value of {num} is {num}")
#Another way
num = int(input("Enter a number: "))
if num < 1:
    abs_value = abs(num)
    print(f"The absolute value of {num} is {abs_value}")
else:
    print(f"The absolute value of {num} is {num}")