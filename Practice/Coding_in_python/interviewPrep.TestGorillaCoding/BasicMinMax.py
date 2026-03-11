def min_max(mylist):
    min = 0
    max = 0
    set_value = True
    for num in mylist:
        if set_value:
            min = num
            max = num
            set_value = False
        elif min > num:
            min = num
        elif max < num:
            max = num
    print(f"minimum value index = {mylist.index(min)}, maximum value index = {mylist.index(max)}")
    return min, max
mylist = [1, 3, 5, 9, 10]
print(min_max(mylist))