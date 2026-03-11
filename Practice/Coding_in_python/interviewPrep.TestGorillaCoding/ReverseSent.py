def rev(sent):
    sen_list = sent.split(" ")
    rev_sen = ""
    for word in sen_list:
        rev_sen = word + " "+ rev_sen
    return rev_sen.strip()
sent = input("Enter a word: ").strip()
print(rev(sent))
