print("These numbers are:")
for num in range(1500, 2310):
    if num % 7 == 0 and num % 5 == 0:
        print(num, end=",")
print("end of series.", end="")