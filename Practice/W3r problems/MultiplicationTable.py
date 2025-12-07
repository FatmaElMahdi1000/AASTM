num = int(input("Enter a number: "))
for n in range(1, 11):
    product = n * num
    if product % 2 != 0:
        print(f"{n} X {num} =", n*num)