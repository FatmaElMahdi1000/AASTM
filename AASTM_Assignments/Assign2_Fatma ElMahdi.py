#Assignment2_Problem #2
name = input("Enter Your Name: ")
year = int(input("Year of birth: "))
current_year = 2020
age = current_year - year

print(f"""what's your name? {name}
On which year, were you born ? {year}
{name} you are {age} years old
""")

#Assignment2_Problem #5
r = int(input("please enter the radius: ")) #Radius can be float? would typecasting to float be better?
pi = 3.14
Diameter = 2*r
area = pi * r**2
circumference = 2 * pi * r

print(f"""
The diameter is: {Diameter}
The area is: {area}
The circumference is: {circumference}
""")

#Assignment2_Problem #6
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
A_mean = (x + y) / 2
H_mean = (2 / ((1/x) + (1/y)))
print(f"""
Arithmetic Mean: {A_mean}
Harmonic Mean: {H_mean}
""")

#Assignment2_Problem #9
Period_of_time = int(input("Enter a period of time (in minutes): "))
hrs_num = Period_of_time // 60 #rounding down to zero_floor
days_num = hrs_num // 24 #rounding down to zero_floor
rem_hrs = hrs_num % 24 #remaining = ((hrs_num / 24) 3.75 - days_num 3) * 24
rem_min = Period_of_time % 60

print(f"{Period_of_time} minutes make {days_num} days, {rem_hrs} hours, and {rem_min} minutes")
