class Solution:
    def productExceptSelf(self, nums):

        product  = []
        updated_list = []
        for i in range(0, len(nums)):
            cp = nums.copy()
            cp.remove(nums[i])
            pro = 1
            for s in cp:
                pro = pro*s
            product.append(pro)
        return product

result = Solution()
res = result.productExceptSelf( [-1,1,0,-3,3])
print(res)