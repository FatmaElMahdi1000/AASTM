word = 'Fatma'

n = len(word) #5
reversed = ' '
for i in range(n - 1, -1 , -1): #len 4
    reversed = reversed + word[i]
print(reversed)