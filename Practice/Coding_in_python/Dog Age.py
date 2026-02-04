Dog_Age = int(input("Enter the dog age: ").strip())

Age = 0
for i in range(1, Dog_Age + 1):
    if i == 1 or i == 2:
        Age += 10.5
    else:
        Age += 4
print(f"Age is {Age}!")