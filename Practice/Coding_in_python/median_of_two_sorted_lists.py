import ast
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        merged = []
        for num1 in nums1:
            merged.append(num1)

        for num2 in nums2:
            merged.append(num2)

        merged = sorted(merged)

        idx = len(merged) // 2

        if len(merged) % 2 == 0:
            median = (merged[idx] + merged[idx - 1]) / 2
            return median
        else:
            median = merged[idx]
            return median

while True:
    user_input = ast.literal_eval(input("Enter a list for nums 1: "))
    try:
        nums1 = user_input
        if not isinstance(nums1, list):
            raise ValueError("Not a list")
        for x in nums1:
            if not isinstance(x, (int, float)):
                raise ValueError("The list must contain digits!")
        break
    except (ValueError, SyntaxError):
        print("Invalid input!")


while True:
    user_input2 = ast.literal_eval(input("Enter a list for nums 2: "))
    try:
        nums2 = user_input2
        if not isinstance(nums2, list):
            raise ValueError("Not a list!")
        for s in nums2:
            if not isinstance(s, (int, float)):
                raise ValueError("The list must contain digits!")
        break
    except (ValueError, SyntaxError):
        print("Invalid input!")


res = Solution()
print("Median = ", res.findMedianSortedArrays(nums1, nums2))


