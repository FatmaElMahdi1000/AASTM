import math
interest = 0.01
loan = 50000
Amount = 0
Month = 1
print("Month", "\t\t", "Amount")
print("-"*20)
while 0 < Month <= 12:
    Amount = int(loan * pow(1 + interest, Month))
    print(Month, "\t\t", Amount)
    Month += 1