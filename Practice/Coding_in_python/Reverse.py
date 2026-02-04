def reverse(word):
    w = " "
    for char in word:
        w = char + w
    return w

word=  "Fatma"
Reversed  = reverse(word)
print(Reversed)