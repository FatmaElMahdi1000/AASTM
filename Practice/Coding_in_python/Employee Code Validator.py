code = input("Enter the code: ").strip()

count = 0
for n in code:
    count+= 1

if 8 <= count <= 12:
    print(True)
else:
    print(False)