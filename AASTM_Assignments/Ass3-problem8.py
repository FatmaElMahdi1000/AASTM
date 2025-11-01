M = int(input("Enter the month: "))
if 1 <= M <= 12:
    if M == 3 or M == 4 or M == 5:
        print("it's Spring!")
    elif M == 6 or M == 7 or M == 8:
        print("it's Summer!")
    elif M == 9 or M == 10 or M == 11:
        print("it's Autumn!")
    else:
        print("it's Winter!")
else:
    print("You Entered invalid month!")

