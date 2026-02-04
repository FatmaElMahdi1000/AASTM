num = input("Enter a number: ").strip()

reversed_num = ""
for n in num:
    reversed_num = n + reversed_num
if num == reversed_num:
    print(True)
else:
    print(False)

