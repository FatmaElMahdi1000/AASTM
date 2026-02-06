# class Solution:
#     def isPerfectSquare(self, num):
#
#         sides = []
#         for i in range(1, num+1):
#             for j in range(i, num+1):
#                 if (i == j) and (i * j == num) and isinstance(i, int) and isinstance(j, int):
#                     sides.extend([i, j])
#         if sides:
#             return True
#         else:
#             return False
#
# res = Solution()
# result = res.isPerfectSquare(4)
# print(result)
class Solution:
    def isPerfectSquare(self, num):
        #binary search /O(log2n)
        if num <2:
            return True

        low  = 2
        high = num
        while low  <= high :
            mid = (high  + low ) // 2 #to give an int if 5.5 then mid is 5
            square = mid * mid #this is our target
            if square == num:
                return True
            elif square < num:
                low = mid  + 1
            else:
                high = mid - 1

        return False
res = Solution()
result = res.isPerfectSquare(14)
print(result)





