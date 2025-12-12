def series_sum(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
nums = [n for n in range(a, b, c)] #(1, 13, 2) /1/3/5/7/9/11.
print(series_sum(nums))