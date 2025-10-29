Devices = int(input("Enter the number of devices: "))
if Devices == 1:
    print("Basic plan. The monthly subscription is 120 EGP")
elif 1 < Devices <= 4:
    print("Premium plan. The monthly subscription is 200 EGP")
else:
    print("Invalid plan. Disallowed number of devices!")

