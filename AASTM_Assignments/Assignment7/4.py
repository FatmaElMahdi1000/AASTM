def std_grade(mark):
    Marks_G1 = [n for n in range(90, 101)]
    Marks_G2 = [n for n in range(80, 90)]
    Marks_G3 = [n for n in range(70, 80)]
    Marks_G4 = [n for n in range(60, 70)]
    Marks_G5 = [n for n in range(50, 60)]
    Marks_G6 = [n for n in range(0, 50)]
    if mark in Marks_G1:
        print("Excellent")
    elif mark in Marks_G2:
        print("Very Good")
    elif mark in Marks_G3:
        print("Good")
    elif mark in Marks_G4:
        print("Satisfactory")
    elif mark in Marks_G5:
        print("Conditional Pass")
    elif mark in Marks_G6:
        print("Fail")
    else:
        print("Invalid Mark")

mark = int(input("Enter student's mark: "))
std_grade(mark)
