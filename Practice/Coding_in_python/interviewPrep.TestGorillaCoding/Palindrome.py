def Palindrome(strParam):
    clean = ""
    for ch in strParam:
        if not ch.isspace():
            clean += ch.lower()

    return clean == clean[::-1]

strParam = input()
print(Palindrome(strParam))