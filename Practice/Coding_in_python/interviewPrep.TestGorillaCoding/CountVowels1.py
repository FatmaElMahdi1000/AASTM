def countv(string):
    vowels = "aeiou"
    count = 0

    for i in range(len(string)): #9
        seen = set()
        for j in range(i,len(string)):
            if string[j] not in vowels:
                break
            else:
                seen.add(string[j])
            if len(seen) == 5:
                count +=1
    return count
string = "cuaieuouac"
    # input().strip()) #removing the extra trailing and leading spaces
print(countv(string))