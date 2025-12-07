my_list = [3, 1, 5, 2, 6, 4, 9]
# Reversed = my_list [::-1]
# print(Reversed)
#
# #longest increasing subsequent
# min = 0

List1 = []
List2= []
for idx in range(len(my_list) - 1):
    if my_list[idx + 1] > my_list[idx]:
        List1.append(my_list[idx])
        List1.append(my_list[idx + 1])
print(List1)