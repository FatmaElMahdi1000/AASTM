st_number = int(input("Enter the number of the students: "))
student_info = []
Avg_list = []
Mark7=0
Mark12=0
participation = 0
Finals = 0
Total_for_Avg = 0

for st in range(1, st_number + 1):
    Total = 0
    name = input("Enter the Name: ")
    Mark_7th = int(input("Enter the 7th Mark: "))
    Mark_12th = int(input("Enter the 12th Mark: "))
    Att = int(input("Enter the participation Mark: "))
    Final = int(input("Enter the Final Mark: "))
    Mark7 = Mark7 + Mark_7th
    Mark12 = Mark12 + Mark_12th
    participation = participation + Att
    Finals= Finals + Final
    Total = Mark_7th + Mark_12th + Att + Final
    Total_for_Avg = Total_for_Avg + Total

    while not(0 <= Total <= 100):
        print("Something is off! Enter the values again!")
        #substracting previous calculated values from incorrect entering
        Mark7 -= Mark_7th
        Mark12 -= Mark_12th
        participation -= Att
        Finals -= Final
        Total_for_Avg -= Total

        name = input("Enter the Name: ")
        Mark_7th = int(input("Enter the 7th Mark: "))
        Mark_12th = int(input("Enter the 12th Mark: "))
        Att = int(input("Enter the participation Mark: "))
        Final = int(input("Enter the Final Mark: "))

        #recalculating the right values in the 2nd attempt.
        Mark7 = Mark7 + Mark_7th
        Mark12 = Mark12 + Mark_12th
        participation = participation + Att
        Finals = Finals + Final
        Total = Mark_7th + Mark_12th + Att + Final
        Total_for_Avg = Total_for_Avg + Total

    info = f"{name}\t\t\t{Mark_7th}\t\t\t{Mark_12th}\t\t\t\t{Att}\t\t\t\t{Final}\t\t\t\t{Total}"
    student_info.append(info)

print("\n")
print("Name\t\t\t7th\t\t\t12th\t\t\tAtt\t\t\tFinal\t\t\tTotal")
print("-"*85)
for row in student_info:
    print(row)

Avg_list.append(Mark7)
Avg_list.append(Mark12)
Avg_list.append(participation)
Avg_list.append(Finals)
Avg_list.append(Total_for_Avg)
print("-"*85)
print("AVERAGE", end="\t\t")

for value in Avg_list:
    print(f"{value/st_number}", end="\t\t\t")
print("-"*85)
