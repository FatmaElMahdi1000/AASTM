grade = int(input("Enter the first grade: "))
counter = 0
total = 0
while 0 < grade <= 100:
    total = total + grade
    grade = int(input("Enter the next grade: "))
    counter += 1
Avg = total / counter
print(Avg)
