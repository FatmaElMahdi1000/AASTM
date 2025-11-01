M = int(input("Enter the month: "))
d = int(input("Enter the day: "))
if 1 <= M <= 12 and 1 <= d <= 31:
    if M == 1 or M == 2:
        print("it's winter!")
    elif M == 4 or M == 5:
        print("it's Spring!")
    elif M == 7 or M == 8:
        print("it's Summer!")
    elif M == 10 or M == 11:
        print("it's Autumn!")
    elif M == 3 and 1 <= d <= 19:
        print("it's winter!")
    elif M == 3 and 20 <= d <= 30:
        print("it's Spring!")
    elif M == 6 and 1 <= d <= 19:
        print("it's Spring!")
    elif M == 6 and 20 <= d <= 30:
        print("it's Summer!")
    elif M == 9 and 1 <= d <= 21:
        print("it's Summer!")
    elif M == 9 and 22 <= d <= 30:
        print("it's Autumn!")
    elif M == 12 and 1 <= d <= 20:
        print("it's Autumn!")
    else:
        print("it's winter!")
else:
    print("You Entered invalid month!")