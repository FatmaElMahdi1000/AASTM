prog_st = int(input("Enter the number of students registered in Programming: "))
prog_st_ids = set()
print("Enter their IDs: ")
for i in range(1, prog_st+1):
    prog_id = int(input(f"Enter ID of Student {(i)}: "))
    prog_st_ids.add(prog_id)

E_st = int(input("Enter the number of students registered in E-learning: "))
E_st_ids = set()
print("Enter their IDs: ")
for i in range(1, E_st + 1):
    E_id = int(input(f"Enter ID of Student ({i}): "))
    E_st_ids.add(E_id)

Multi_st = int(input("Enter the number of students registered in Multimedia: "))
Multi_st_ids = set()
print("Enter their IDs: ")

for s in range(1, Multi_st + 1):
    Multi_id = int(input(f"Enter ID of Student ({s}): "))
    Multi_st_ids.add(Multi_id)

print(prog_st_ids)
print(E_st_ids)
print(Multi_st_ids)

print(f"Common students at Programming and E-learning:", prog_st_ids.intersection(E_st_ids))
print(f"Common students at Programming and Multimedia:", prog_st_ids.intersection(Multi_st_ids))
print(f"Common Students at E-learning and Multimedia:", E_st_ids.intersection(Multi_st_ids))
print(f"Common Students at all three courses:", prog_st_ids.intersection(E_st_ids,Multi_st_ids))