def IntCount(arr, val,n):
    smaller = 0
    larger = 0
    EqualTo = 0
    #0 1 2 3
    array = arr.split(" ")
    array = [int(n) for n in array]
    for i in range(0, n):
        if array[i] < val: #
            smaller+=1
        elif array[i] == val:
            EqualTo+=1
        else:
            larger+=1
    return f"{smaller}{EqualTo}{larger}"
n = 5
val = 6
arr = input()
print(IntCount(arr, val,n))
