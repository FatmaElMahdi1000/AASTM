salary = int(input("Enter the employee's salary: "))
years = int(input("Enter the year's of service: "))
if years >= 4:
    if 4  <= years <8:
        Bonus = salary * 0.05
    elif 8 <= years <12:
        Bonus = salary * 0.10
    else:
        Bonus = salary * 0.20
print(f"Bouns is {Bonus} pounds")