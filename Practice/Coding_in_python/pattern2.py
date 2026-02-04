# for r in range(1, 5):
#     for c in range(r,0, -1):
#         print(c, end="")
#     print()




for r in range(1, 5):
    print(" "* r*5, end="")
    for c in range(r, 0, -1):
        print(c, end="")
    print()