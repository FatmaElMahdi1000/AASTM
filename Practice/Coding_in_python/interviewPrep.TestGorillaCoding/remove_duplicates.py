def duplicates(my_list):
    udt_list = set(my_list)
    return list(udt_list)

my_list = [1,2,2,3,1]
print(duplicates(my_list))