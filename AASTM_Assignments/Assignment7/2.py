def func(m, n):
    for num in range(m, n+1):
        if num % 2 != 0:
            print(num)

m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))
func(m, n)