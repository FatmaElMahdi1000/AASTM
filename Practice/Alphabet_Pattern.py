#Z shape
# for r in range(1, 8):
#     if r == 1 or r == 7:
#         print("*" * 7)
#     else:
#         print(" " * (7 - r) + "*")

#T shape
for r in range(1, 6):
    if r == 1:
        print("*" * 5, end="")
    else:
        print(" "*2 + "*" + " "*2,  end="")
    print()