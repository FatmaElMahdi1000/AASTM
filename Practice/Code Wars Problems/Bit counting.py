#converting from Decimal to Binary.
def count_bits(n):
    binary_repr = ""
    digit_count = 0
    if n == 0:
        binary_repr += "1"
        digit_count += 1
    while n != 0: #1
        remainder = n % 2
        n = n // 2
        if remainder != 0:
            binary_repr += "1"
            digit_count += 1
        else:
            binary_repr += "0"
            digit_count += 1
    return binary_repr, digit_count

n = int(input("Enter a number: "))
print(count_bits(n))




