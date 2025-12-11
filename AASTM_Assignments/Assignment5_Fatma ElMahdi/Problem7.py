st_number = int(input("Enter the number of the students: "))
student_info = []

for st in range(1, st_number + 1):
    Total = 0
    name = input("Enter the Name: ")
    Mark_7th = int(input("Enter the 7th Mark: "))
    Mark_12th = int(input("Enter the 12th Mark: "))
    Att = int(input("Enter the participation Mark: "))
    Final = int(input("Enter the Final Mark: "))
    Total = Mark_7th + Mark_12th + Att + Final

    while not(0 <= Total <= 100):
        print("Something is off! Enter the values again!")
        name = input("Enter the Name: ")
        Mark_7th = int(input("Enter the 7th Mark: "))
        Mark_12th = int(input("Enter the 12th Mark: "))
        Att = int(input("Enter the participation Mark: "))
        Final = int(input("Enter the Final Mark: "))
        Total = Mark_7th + Mark_12th + Att + Final
    info = f"{name}\t\t\t{Mark_7th}\t\t\t{Mark_12th}\t\t\t\t{Att}\t\t\t\t{Final}\t\t\t\t{Total}"
    student_info.append(info)

print("Name\t\t\t7th\t\t\t12th\t\t\tAtt\t\t\tFinal\t\t\tTotal")
print("-"*80)
for row in student_info:
    print(row)


