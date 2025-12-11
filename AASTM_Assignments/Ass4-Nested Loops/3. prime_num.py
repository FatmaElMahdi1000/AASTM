print("Prime Numbers below 100: \n")

for num in range (2, 100):
    for n in range(2, num):
        if num % n == 0:
            break
    else:
        print(num)




