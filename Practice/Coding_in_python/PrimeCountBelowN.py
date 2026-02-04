n = int(input("Enter a number: "))

count = 0

i = 2
while i <= n:
    for x in range(2, i):
        if i % x == 0:
            break
    else:
        count += 1
    i+=1
print(count)