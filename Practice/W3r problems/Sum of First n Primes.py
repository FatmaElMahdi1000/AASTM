sum = 0

n = int(input("Enter a number (0 to exit, n <= 10000): "))
while n > 10000:
    n = int(input("Enter another valid number: "))

count = 0  # how many primes we have summed
i = 2      # start checking from 2

while count < n:  # sum exactly n primes
    for x in range(2, i):
        if i % x == 0:
            break
    else:
        sum += i
        count += 1
    i += 1

print(f"Sum of first {n} prime numbers: {sum}")
