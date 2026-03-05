def product(arr, n):
    rearr=[]
    array = arr.split(" ")
    array = [int(n) for n in array]
    for i in range(0, n): #i = 2
        prod = 1
        arr_cp = array.copy() #1 2 3 4
        arr_cp.pop(i) #1 3 4
        for num in arr_cp:
            prod = prod*num
        rearr.append(prod)
    return rearr

n = 4
arr = input()
print(product(arr, n))
