my_list = []
i = 1
for i in range(i, 11):
    my_list.append(i)
print(my_list)

print("____Another Way_____")

List_A = list(range(1,11))

print("___ Converting a list of ints to a list of strings____ ")
updated_list = list(map(str, List_A))
print(updated_list)

print("___Multiplying all elements in a list by 2.__WAY1__ ")
List_A = list(range(0, 11))
updated_list = []
for num in List_A:
    updated_list.append(num*2)
print(updated_list)

print("___Multiplying all elements in a list by 2.__WAY2__ ")
updated_list = [num * 2 for num in List_A]
print(updated_list)