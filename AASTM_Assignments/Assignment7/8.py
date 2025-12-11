def avg(nums, count):
    sum = 0
    for n in nums:
        sum += n
    average = sum / count
    return average

count = 5
nums = [int(input("Enter a number: ")) for _ in range(0,count)]
result = avg(nums, count)
print(result)