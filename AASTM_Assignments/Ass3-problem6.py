classes_num = float(input("Enter the number of classes held: "))
attended_num = float(input("Enter the number of classes attended: "))
Percentage = (attended_num / classes_num) * 100
if 0 < Percentage < 75:
    print(f"Attendance is {Percentage} %")
    print("You're Not allowed to enter the exam!")
else:
    print(f"Attendance is {Percentage} %")
    print("You can enter the final exam!")
