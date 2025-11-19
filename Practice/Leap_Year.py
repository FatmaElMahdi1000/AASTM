year = int(input("Enter a year: "))
if year % 4 == 0 and year % 100 != 0:
    print("it's a leap year!")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print(" a leap year!")
else:
    print("it's not a leap year!")

#can be simplified to be:
# year = int(input("Enter a year: "))
#
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("It's a leap year!")
# else:
#     print("It's not a leap year!")