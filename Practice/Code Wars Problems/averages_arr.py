def averages(arr):
    updated_arr = []
    if 1 in arr or 0 in arr or not arr:
        return []
    else:
        for i in range(0, len(arr)-1):
            updated_arr.append((arr[i] + arr[i+1])/2)
        return updated_arr

arr = [2,3,8,3]

print(averages(arr))