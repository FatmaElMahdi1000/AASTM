def ListOrTuple(Numbers):
    My_list = []
    for char in Numbers:
        if char != ',' and char != ' ':
            My_list.append(int(char))
    return "List: ", My_list, "Tuple: ", tuple(My_list)

Numbers = input("Enter number of numbers: ")
Result = ListOrTuple(Numbers)
print(Result)
