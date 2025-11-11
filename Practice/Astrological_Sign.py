def sign(day, month):
    if (month == 1 and 20 <= day <= 30) or (month == 2 and 1 <= day <= 18):
        return "your sign is Aquarius"
    elif (month == 2 and 19 <= day <= 30) or (month == 3 and 1 <= day <= 20):
        return "your sign is Pisces"
    elif (month == 1 and 1 <= day <= 19) or (month == 12 and 22 <= day <= 31):
        return "your sign is Capricorn"
    elif (month == 11 and 22 <= day <= 30) or (month == 12 and 1 <= day <= 21):
        return "your sign is Sagittarius"
    elif (month == 7 and 23 <= day <= 30) or (month == 8 and 1 <= day <= 22):
        return "your sign is Leo!"
    else:
        return "Sorry, we cannot find your zodiac in this set! :P"

while True:
    month = input("Enter the Month: ").strip()
    try:
        month = int(month)
        if month != "":
            if 1 <= month <= 12:
                break
        else:
            continue
    except ValueError:
        print("Enter a valid month!")
        continue

while True:
    day = input("Enter the birthday: ").strip() #string
    try:
        day = int(day)
        if day != "":
            if 1 <= day <= 31:
                break
            else:
                continue
    except ValueError:
        print("Please enter a valid number.")
        continue

Your_Zodiac = sign(day, month)
print(Your_Zodiac)