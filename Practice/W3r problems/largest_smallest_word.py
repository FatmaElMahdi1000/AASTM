string1 = "Hi there this is Fatma"
string2 = "hi"

for c in string2.lower():
    if c in string1:
        string1 = string1.replace(c.upper(), "")
        string1 = string1.replace(c.lower(), "")
print(string1)