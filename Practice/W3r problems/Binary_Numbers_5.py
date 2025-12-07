Binary = input("Binary numbers: ")
Binary_list = Binary.split(",")
updated_list = []
for num in Binary_list:
    if (int(num) % 5) == 0:
        updated_list.append(num)
    else:
        pass
print(updated_list)