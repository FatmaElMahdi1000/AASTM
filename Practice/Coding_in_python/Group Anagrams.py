# from collections import defaultdict
# class Solution:
#     def groupAnagrams(self, strs):
#         ans = {}
#         for word in strs:
#             sorted_word = "".join(sorted(word))
#             if sorted_word not in ans:
#                 ans[sorted_word] = []
#             ans[sorted_word].append(word) #we're appending to [] (dictionary value)
#         return list(ans.values())
#
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# result= Solution()
# res = result.groupAnagrams(strs)
# print(res)

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        hash_table = defaultdict(list) #dictionary = {} but we can say dictionary = defaultdict(list), it creates values of that dictionaries as lists.
        #then we can append to the lists our values
        for word in strs:
            sorted_word = "".join(sorted(word))
            hash_table[sorted_word].append(word)
        return list(hash_table.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result= Solution()
res = result.groupAnagrams(strs)
print(res)

