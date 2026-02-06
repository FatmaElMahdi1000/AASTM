class Solution:
    def longestWord(self, words):
        ans = ""
        words.sort()
        wordset = set(words)
        for word in words:
            if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                for k in range(1, len(word)):
                    if (word[:k] in wordset):
                        ans = word
        return ans


words = ["banana", "apple", "apply", "app", "ap", "a"]
print(Solution().longestWord(words))



