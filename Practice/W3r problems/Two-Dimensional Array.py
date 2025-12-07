def grid(r, c):

    arr = []
    for i in range(0, r):
        arr2 = []
        for j in range(0, c):
            arr2.append(i * j)
        arr.append(arr2)
    return arr

r = 3
c = 4

dimensional_arr = grid(r, c)
print(dimensional_arr)