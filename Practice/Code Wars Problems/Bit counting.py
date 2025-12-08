#converting from Decimal to Binary, getting the count of "1"s only in the binary rep
def count_bits(n):
    binary_repr = ""
    digit_count = 0
    while n != 0: #1
        remainder = n % 2
        n = n // 2
        if remainder != 0:
            binary_repr += "1"
            digit_count += 1
        else:
            binary_repr += "0"
    return binary_repr, digit_count

n = int(input("Enter a number: "))
print(count_bits(n))




