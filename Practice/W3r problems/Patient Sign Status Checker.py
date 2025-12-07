PHR = int(input("Enter the patient heart rate: "))
counter = 0
Tachycardia = 0
while(PHR != -1):
    if 0 < PHR < 60:
        print("Condition is: Bradycardia!")
    elif(60 <= PHR <= 100):
        print("Condition is: Normal!")
    else:
        print("Condition is: Tachycardia!")
        Tachycardia += 1
    counter += 1
    PHR = int(input("Enter the patient heart rate: "))

print(f"Total Reading_num = {counter}, {Tachycardia} Tachycardia")
