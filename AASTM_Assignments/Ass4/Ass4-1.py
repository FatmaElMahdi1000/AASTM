M = int(input("The First number: "))
N = int(input("The Last number: "))

sum = 0
for num in range(M, N + 1):
    if num % 2 == 0:
        sum += num
print(sum)