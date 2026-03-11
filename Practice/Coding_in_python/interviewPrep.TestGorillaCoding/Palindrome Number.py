def isPalindrome(x):
    y = str(x)
    reversed = y[::-1]
    return y == reversed


x = 121
print(isPalindrome(x))