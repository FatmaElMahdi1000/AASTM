class Solution:
    def kthGrammar(self, n, k):
        content = '0'
        if k == 1 and n == 1:
            return int(content)
        else:
            for i in range(2, n+1):
                new_content = ''  # 01
                for char in content:
                    if char == "0":
                        new_content += "01"
                    else:
                        new_content += "10"
                content = new_content
            return int(content[k-1])

n = 2
k = 2
result = Solution()
res = result.kthGrammar(n, k)
print(res)