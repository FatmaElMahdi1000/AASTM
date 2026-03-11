#Have the function VowelCount(str
# take the str string parameter being passed and return the
# number of vowels the string contains (ie. “All cows eat grass and moo” would return 8).
# Do not count y as a vowel for this challenge.

def countvowels(string):
    vowels = "aioeu"
    count = 0
    #REVEW LOWER()
    for ch in string.lower():
        if ch in vowels:
            count += 1
    return count

string = "All cows eat grass and moo"
print(countvowels(string))
