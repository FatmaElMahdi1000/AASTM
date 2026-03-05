class Solution:
    def topKFrequent(self, nums, k):
        hash_table = {}
        for n in nums:
            hash_table[n] = hash_table.get(n, 0)+1
        Final = []

        i = 1
        while hash_table and i <= k: #i = 1
            max_item = max(hash_table.items(), key=lambda x: x[1])
            Final.append(max_item[0])
            del hash_table[max_item[0]]
            i+=1
        return Final

nums  = [1,2,3,4,2,2,2,1]
k = 2
result = Solution()
res =  result.topKFrequent(nums, k)
print(res)