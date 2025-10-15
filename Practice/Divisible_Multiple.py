def number(number_list_ranges):
    Start_num = number_list_ranges[0]
    End_num = number_list_ranges[1]
    Num_list = []
    for num in range(Start_num, End_num + 1):
        Num_list.append(num)
    Updated_list = []
    for num in Num_list:
        if num % 7 == 0 and num % 5 == 0:
            Updated_list.append(num)
    return Updated_list

number_list_ranges = (1500, 2700) #tuple (start num, end num)
Result = number(number_list_ranges)
print(Result)
