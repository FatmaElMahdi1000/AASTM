def mysum(arr, n):
    array = arr.split(" ")
    array_val = [int(x) for x in array]
    rearr = []
    for i in range(0, n):
        arr_cp = array_val.copy()
        arr_cp.pop(i)
        total = sum(arr_cp)
        rearr.append(total)
    return rearr

arr = input()
n = 5
print(mysum(arr, n))