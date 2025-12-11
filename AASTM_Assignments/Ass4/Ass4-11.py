num = input("Enter a number: ").strip()
while not num.isdigit():
    num = input("Enter a valid number: ").strip()


count = 0
for n in num:
    count += 1
print(count)