#sorting the search interval
from random import choice
def sorted_list(list_num):
    list_num.sort()
    return list_num

def Binary_search(Sorted_interval, target):

    list_len = len(Sorted_interval)
    low_idx = 0
    high_idx = list_len - 1

    while low_idx <= high_idx:
        Mid_idx = (high_idx + low_idx) // 2  # floor is rounding num down when, it's positive
        if Sorted_interval[Mid_idx] < target:
            low_idx = Mid_idx + 1
            high_idx = list_len - 1
        elif Sorted_interval[Mid_idx] > target:
            low_idx = 0
            high_idx = Mid_idx - 1
        else:
            return f"The target is at index : {Mid_idx}"

list_num = [10, 4, 11, 9, 1, 0]
Sorted_interval = sorted_list(list_num)
target = choice(Sorted_interval)
print(Sorted_interval)
print("Target is: ", target)
print(Binary_search(Sorted_interval, target))
