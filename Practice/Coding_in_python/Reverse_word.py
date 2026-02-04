def reverse(word):
    reversed = ""
    for char in word:
        if char.isalpha(): #checking if the character is part of the alphabet
            reversed = char.lower() + reversed #making it all lower
        else: #if character is not alpha() or part of alphabet
            continue #it skips the rest of the loop body and jumps straight to the next iteration.
    return reversed

word = 'Fat1a'
Reversed_word = reverse(word)
print(Reversed_word)