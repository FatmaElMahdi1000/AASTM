period_in_min = int(input("Enter period (in min): "))
hrs = period_in_min // 60 #comparison of min to min
min_remaining = period_in_min % 60
days = hrs // 24 #hrs to hrs.
days_remaining = hrs % 24


print(hrs)
print(days)
print(days_remaining)
print(min_remaining)