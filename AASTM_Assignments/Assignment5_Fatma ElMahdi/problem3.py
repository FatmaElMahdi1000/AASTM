i = 1
nums = []
while i < 11:
    while True:
        try:
            num = int(input("Enter a number: ").strip())
            break
        except ValueError:
            print('invalid number!')
    nums.append(num)
    i += 1
print(f"List before sorting: {nums}")
nums.sort(reverse=True)
print(f"List after sorting(Descending Order): {nums}")

#Getting the highest 3 items
nums_copy = nums[:]
highest_three = []
while len(highest_three) < 3:
    maximum = max(nums_copy)
    if maximum not in highest_three:
        highest_three.append(maximum)
    nums_copy.remove(maximum)
print(f"Highest three items: {highest_three}")