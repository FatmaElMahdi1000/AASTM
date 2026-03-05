from sqlalchemy import false


def isValidExpression(exp):
    br_table = {"}": "{", "]": "[" ,")": "("}
    stack = [] #for storing opening brackets
    for ch in exp:
        if ch in br_table:
            if not stack:
                return False
            top = stack.pop() #{
            if top != br_table[ch]: #if top { does not equal the value of the char }
                return False
        else:
            stack.append(ch)
    if stack: #stack must be empty if it's non-empty means no matches.
        return False
    else:
        return True
exp = input("Enter an expression: ")
print(isValidExpression(exp))
#([{}])