# max = 0
# min = 100
# i = 0
# while i < 3:
#     num = int(input("Enter a number: "))
#     if min > num:
#         min = num
#     if max < num:
#         max = num
#     i += 1
# print(f"max : {max}, min = {min}")

#another way to do it if we don't have a ceiling of max nums
set_values = True
i = 0
while (i < 3):
    num = int(input("Enter a number: "))
    if set_values == True:
        max = num
        min = num
        set_values = False
    if max < num:
        max = num
    if min > num:
        min = num
    i += 1
print(min)
print(max)




























