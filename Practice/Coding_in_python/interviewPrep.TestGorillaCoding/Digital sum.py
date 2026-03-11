def DigitalSum(arr):
    udt_arr = []
    for ch in arr:
        if ch.isdigit() and not ch.isspace():
            udt_arr.append(int(ch))
    return sum(udt_arr)

arr  = input()
print(DigitalSum(arr))