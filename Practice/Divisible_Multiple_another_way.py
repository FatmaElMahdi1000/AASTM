def calculations(num_list):

    updated_list = []
    for num in num_list:
        if num % 5 == 0 and num % 7 == 0:
            updated_list.append(num)
    return len(updated_list)

num_list = [num for num in range(1500, 2701)] #shortcut of for

Result = calculations(num_list)
print(Result)
