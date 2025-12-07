def calculation(num):
    if isinstance(num, int):
        sum = 0
        for i in range(0, 3):
            if i == 0:
                sum = sum + num
            elif i == 1:
                updated_num = str(num) * 2
                sum = sum + int(updated_num)
            elif i == 2:
                updated_n = str(num) * 3
                sum = sum + int(updated_n)
        return sum

num = 5
Result = calculation(num)
print(Result)