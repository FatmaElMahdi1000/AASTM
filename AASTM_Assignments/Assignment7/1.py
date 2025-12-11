def func(nums):
    for num in nums:
        if num %2 != 0:
            print(num)
nums = []
for n in range(1, 10):
    nums.append(n)
func(nums)