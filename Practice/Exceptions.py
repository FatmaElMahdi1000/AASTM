def nums(num_list):
    Updated_list = []
    for num in num_list:
        if num != 3 and num != 6:
            Updated_list.append(num)
    return Updated_list



num_list = [num for num in range(0, 7)]
Result = nums(num_list)
print(Result)