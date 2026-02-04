def line_Seq():

    lines = ""
    line_len = 0

    while True: #Keep doing what's in the loop indefinitely until something breaks it:)
        sent = input("Enter a sentence: ")
        lines = lines + "\n" + sent
        line_len += 1
        if line_len == 5:
            break
    return lines.upper()

Result = line_Seq()
print(Result)