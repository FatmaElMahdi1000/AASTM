cents = int(input("Enter cents: "))
leftover_cents = cents % 100
dollars = (cents - leftover_cents) / 100
print(leftover_cents)
print(dollars)