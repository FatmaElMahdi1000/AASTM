from datetime import date
date1 = date(2025, 10, 2)
date2 = date(2025, 10, 19)

delta = date2 - date1
print(delta.days)