num = input("Enter a number: ")

if "-" in num:
    abs = -1 * int(num)
    print(f"the absolute value is: {abs}")
elif not "-" in num:
    print(f"the absolute value is: {int(num)}")

