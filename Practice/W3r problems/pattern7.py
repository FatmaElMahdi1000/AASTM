for r in range(1, 10):
    if r == 1 or r == 9:
        print("  ", "***", "  ")
    elif r == 2 or r == 8:
        print(" *", "   ", "*")
    elif 3 <= r <= 7:
        print("*       *")
    else:
        print()
