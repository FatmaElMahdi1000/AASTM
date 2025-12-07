for r in range(6, -1, -1):
    space =  6- r
    print(" " * space, "*", end="")
    if r > 0:
        print(" " * (2*r- 1), "*", end="")
    print()

for r in range(1, 7):
    space =  6- r
    print(" " * space, "*", end="")
    if r > 0:
        print(" " * (2*r- 1), "*", end="")
    print()