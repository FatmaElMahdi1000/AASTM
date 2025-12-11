num = int(input("Enter a number: "))

print("\t\t", end="")
for i in range(1, 11):
    print(" ", i, "\t", end="")
print()
print("-" * 85)
for r in range(1, num + 1):
    print(" ", r, "\t", end="")
    for c in range(1, 11 ):
        print(" ", r*c, "\t", end="")
    print()