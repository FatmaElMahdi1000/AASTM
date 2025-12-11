for r in range(9, 0, -1):
    if r < 9:
        diff = 9 - r #r = 8, diff is 1 in the 1st iteration
        print(" " * diff, "*"* r)