Apples = int(input("Enter a number of Apples: "))
Dozens_of_apples = Apples % 12 #left over apples
Dozens_at_hand = (Apples - Dozens_of_apples) / 12
print(f"Leftovers:{Dozens_of_apples}")
print(f"Apples at hand:{Dozens_at_hand}")