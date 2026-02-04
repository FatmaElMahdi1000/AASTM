def string_reversing(sen):
    sublist = sen.split()
    reversed = " "
    for word in sublist:
        reversed = word + " " + reversed
    return reversed


sen = input("Enter a sent. to reverse: ").strip() #to remove(leading, trailing spaces or new line character
final_result = string_reversing(sen)
print(final_result)