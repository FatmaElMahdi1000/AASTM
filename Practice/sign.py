year = int(input("Enter the year: "))

Zodiac= {1: "Dragon", 2: "snake", 3: "OX", 4: "horse",5: "Monkey"}
# for key, item in Zodiac.items():
#     if(year - 2000) % 12 == key:
#         print(item)

idx = (year - 2000) % 12
print(f"The chinese zodiac is: {Zodiac[idx]}")