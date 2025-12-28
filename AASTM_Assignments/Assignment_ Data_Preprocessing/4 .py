import pandas as pd

students = {}
students['Group A & B'] = []
st_A_num = int(input("Enter the number of students in Group (A): "))
for st_A in range(1, st_A_num+1):
    a = input(f"Student ({st_A}): ").capitalize().strip()
    students['Group A & B'].append(a)

st_B_num = int(input("Enter the number of students in Group (B): "))
for st_B in range(1, st_B_num+1):
    b = input(f"Student ({st_B}): ").capitalize().strip()
    students['Group A & B'].append(b)

print("The students in alphabetical order: ")

students['Group A & B'] = sorted(students['Group A & B'])
data = pd.DataFrame(students)
data.insert(0, "ID", [f"{x}." for x in range(1, len(data) + 1)])
print(data[['ID', 'Group A & B']].to_string(index=False, header=False))
