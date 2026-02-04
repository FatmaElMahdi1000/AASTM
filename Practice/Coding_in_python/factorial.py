print(f"Number\tFactorial\tSum")
factorial = 1
sum = 0
for i in range(1, 6):
    factorial = factorial * i
    sum += i
    print(f"{i}\t\t{factorial}\t\t\t{sum}")