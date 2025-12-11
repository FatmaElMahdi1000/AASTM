def pattern(r, c):
    for i in range(0, r):
        for j in range(0, c):
            print("*", end="")
        print()


r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
pattern(r, c)