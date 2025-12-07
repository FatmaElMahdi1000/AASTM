import calendar

def calender_printer(month, year):
    return calendar.month(year, month)

month = int(input())
year = int(input())
Your_Calender = calender_printer(month, year)
print(Your_Calender)