def getMaxChars(s):
    Frequency = {}
    for char in s:
        if not char.isspace():
            Frequency[char] = Frequency.get(char, 0) + 1
                                         #x[1] means maximum based on the value not the key
    max_item = max(Frequency.items(), key=lambda x: x[1])
    return max_item[0]

s = input()
print(getMaxChars(s))

# def get_max_chars(s):
#     frequency = {}
#     max_frequency = 0
#     max_char = '\0'
#     # Skip leading whitespace characters
#     i = 0
#     while i < len(s) and s[i].isspace():
#         i += 1
#     # Calculate the frequency of each character
#         while i < len(s):
#             current_char = s[i]
#             frequency[current_char] = frequency.get(current_char, 0) + 1
#             if frequency[current_char] > max_frequency:
#                 max_frequency = frequency[current_char]
#                 max_char = current_char
#             i += 1
#     return max_char
# s = input("Enter a string: ").strip()
# res = get_max_chars(s)
# print(res)
