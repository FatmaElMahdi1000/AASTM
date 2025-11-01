classes_num = float(input("Enter the number of classes held: "))
attended_num = float(input("Enter the number of classes attended: "))
Percentage = (attended_num / classes_num) * 100
if Percentage < 75:
    print(f"Attendance is {Percentage} %")

    ans = input("Do you've a medical cause(Y/N)? ")
    while True: #while we've an input in answer/while True
        if not(ans.upper() == 'Y' or ans.upper() == 'N'):
            print("Invalid answer!")
            ans = input("Do you've a medical cause(Y/N)? ")
        else:
            if ans.upper() == 'Y':
                print("You can enter the final exam!")
                break
            else:
                print("You're not allowed to enter the final exam!")
                break
else:
    print(f"Attendance is {Percentage} %")
    print("You can enter the final exam!")
