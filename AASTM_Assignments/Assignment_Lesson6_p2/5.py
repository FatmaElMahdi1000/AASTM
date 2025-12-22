st_ids = set()
st_no = int(input("Enter the number of the students: "))
for i in range(1, st_no+1):
    id = input(f"Enter ID of Student ({i}): ")
    if 1 <= int(id) <= 9999:
        st_ids.add(id)
    else:
        continue
print("The registered students are:", st_ids)
