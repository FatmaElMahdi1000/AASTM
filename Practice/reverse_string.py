def reverse(sen):
    #reversed_sen = ''.join(reversed(sen))  #ANOTHER WAY
    #return(reversed_sen)

    reversed_sen = " "
    for char in sen:
        reversed_sen = char + reversed_sen
    return reversed_sen

sen = "Hi there!"
print(reverse(sen))