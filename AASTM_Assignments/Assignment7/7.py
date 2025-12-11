def product(nums):
    product = 1
    for n in nums:
        product *= n
    return product

nums = [int(input("Enter a number: ")) for _ in range(0,3)]
product_result = product(nums)
print(product_result)