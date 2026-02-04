for r in range(1, 6):
    for c in range(1, 6):
        if (c - r) % 2 == 0 :
            print("O", end="")
        else:
            print("X", end="")
    print()