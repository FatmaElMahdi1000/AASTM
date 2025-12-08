binary_repr = ""
digit_count = 0
number = 4
division_int = number / 2
if number == 0:
    binary_repr += "1"
    digit_count += 1
while number != 0: #1
    remainder = number % 2
    number = number // 2
    if remainder != 0:
        binary_repr += "1"
    else:
        binary_repr += "0"
    digit_count += 1

print(binary_repr[::-1])
print(digit_count)



