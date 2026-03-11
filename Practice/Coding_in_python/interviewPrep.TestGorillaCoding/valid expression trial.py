def isValidExpression(exp):
    closed_opened = {"}": "{", ")":"(", "]": "[" }
    stack = []
    for br in exp:
        if br in closed_opened:
            if stack:
                top = stack.pop()
                if top != closed_opened[br]:
                    return False
        else:
            stack.append(br)

    if stack:
        return False
    else:
        return True
exp = input("Enter an expression: ")
print(isValidExpression(exp))
#([{}])