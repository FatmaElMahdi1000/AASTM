Word =  "Madam"

Reversed_Word = ""
for char in Word:
    Reversed_Word = char.lower() + Reversed_Word

if Word.lower() == Reversed_Word.lower():
    print("This is a palindrome!")
else:
    print("This is not a palindrome!")
