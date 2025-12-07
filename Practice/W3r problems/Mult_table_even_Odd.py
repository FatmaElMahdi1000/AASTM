print('\t', end="")
for i in range(1, 13):
    print('\t', i, end="")
print()
print("-" * 85)
for r in range(1, 6):
    print("\t", r, end="")
    for c in range(1, 13):
        if (r * c)% 2 != 0:
            print("\t", "-", end="")
        if (r * c) % 2 == 0:
            print("\t", r * c, end="") #printing evens only
    print()