def maskify(cc):
    remaining_ch = len(cc) - 4
    return cc.replace(cc[:-4], ("#"*remaining_ch))

cc = input("Enter your phone number: ").strip() #to remove any new lines or additional spaces.
result = maskify(cc)
print(result)
