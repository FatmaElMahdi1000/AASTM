num_list = []

i = 0
while i < 5:
    num = int(input("Enter a num: "))
    num_list.append(num)
    i += 1
# num_list_len = len(num_list)
# for n in range(0, num_list_len): #n is idx
#     rep = 0
#     for j in range(0, num_list_len):#j is idx
#         if num_list[n] == num_list[j]:
#             rep += 1
#     if rep > 1:
#         print(f" some numbers are repeated!")
#         break
#

#Comparing the list length with its conversion to a SET:
num_list_length = len(num_list)

num_set = set(num_list)
if num_list_length == len(num_set):
    # If the lengths are equal, it means all elements in the list are distinct.
    print("Elements in the list are distinct")
else:
    print("Some elements are repeated")
