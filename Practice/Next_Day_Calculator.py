year = int(input("Enter a year: "))
Month = int(input("Enter a Month: "))
Day = int(input("Enter a day: "))

while True:
    if not (1 <= Month <= 12):
        print("Invalid Month!")
        Month = int(input("Enter the Month again: "))
        continue #Without continue, the code below would still execute even though the month is invalid
    if not (1 <= Day <= 31):
        print("Invalid Day!")
        Day = int(input("Enter the day again: "))
        continue#Without continue, the code below would still execute even though the month is invalid

    print(f"the current date = {year} - {Month} - {Day}!")

    next_day = input("Do you want the next date? (y/n): ").lower()
    if next_day != "y":
        break

    Day += 1
    if Day > 30:
        Month += 1
        Day = 1

    if Month > 12:
        year += 1
        Month = 1



