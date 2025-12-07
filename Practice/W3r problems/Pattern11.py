for r in range(1, 8):
    print(r * " ", end="")
    for c in range(8, r, -1):
        print("X", end=" ")
    print()