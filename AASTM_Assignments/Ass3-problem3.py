Units_num = int(input("Enter the number units (in KW): "))
if Units_num < 1:
    print("Invalid no. of units!")
elif 1 <= Units_num <= 99:
    M_consumption = 0.15 * Units_num
elif 100 <= Units_num <= 199:
    M_consumption = 0.30 * Units_num
elif 200 <= Units_num <= 299:
    M_consumption = 0.40 * Units_num
else:
    M_consumption = 0.50 * Units_num
print(f"Your Monthly consumption is {Units_num} and your total bill is {M_consumption} pounds!")