
for r in range(1, 6):

    spaces = 5 - r // 2
    print(" " * spaces, end="")
    for c in range(1, r+1):
        print( c,end="")
    for n in range(r-1, 0,-1):
        print(n, end="")
    print()

