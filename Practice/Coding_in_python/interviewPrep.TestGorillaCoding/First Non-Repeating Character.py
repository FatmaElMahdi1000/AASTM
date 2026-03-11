def non_rep(TheString):
    Table = {}
    for ch in TheString:
        Table[ch] = Table.get(ch, 0) + 1
    for ch in Table:
        if Table[ch] == 1:
            return ch
    return ""

TheString = input()
print(non_rep(TheString))