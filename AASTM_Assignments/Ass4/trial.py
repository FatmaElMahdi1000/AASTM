n = 1
for r in range(1, 5):
    spaces = 4 - r
    print(" " * spaces, end="")
    for c in range(1, r+1):
        print(n, " ", end="")
        n+= 1
    print()
