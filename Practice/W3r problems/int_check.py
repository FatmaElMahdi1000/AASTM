string = input("Enter a random string: ").strip() #removing new lines
#
# if string.isdigit():
#     print("String is integer!")
# else:
#     print("String is not integer!")

for char in string:
    if char.isalpha(): #if the character is part of the alphabet
        print("String is not integer!")
        break
else:
    print("String is an integer!")