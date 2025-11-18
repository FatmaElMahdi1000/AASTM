for r in range(1, 8):
    if r == 1 or r == 7:
        print("*" * 7)
    else:
        print(" " * (7 - r) + "*")
