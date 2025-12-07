#problem1
# Apples = int(input("Enter the number of Apples: "))
# Dozens = Apples // 12
# left_overs = Apples % 12
# print(f"Dozens:{Dozens}!")
# print(f"left_overs:{left_overs}!")

#problem2
# Dis_Meters = int(input("Enter the distance in meters: "))
# kiloMeters = Dis_Meters // 1000
# Left_meters = Dis_Meters % 1000
# print(f"KiloMeters {kiloMeters}, Meters Left: {Left_meters}")

#Problem3
Date = int(input("Enter a date in this format: "))
year = Date//10000
updated_date = Date % 10000 #20211231 ÷ 10000 = 2021 remainder 1231
month = updated_date//100
day = updated_date % 100
print(updated_date)
print(year)
print(month)
print(day)
print(f"the date is {year} / {month} / {day}")







