print("The first ten prime numbers are:")
prime_nums = []
ten_primes = ""
for num in range (2, 100):
    for n in range(2, num):
        if num % n == 0:
            break
    else:
        prime_nums.append(num)
i = 0
while i < 10:
    ten_primes = ten_primes + " " + str(prime_nums[i])
    i += 1
print(ten_primes)


