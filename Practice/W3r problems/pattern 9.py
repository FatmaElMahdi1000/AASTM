# for i in range(1, 5):
#     print(" " * (5 - i - 1) + "*", end="")
#     if i > 1:
#         print(" " * (2*i - 1) + "*", end="")
#     print()
#
# for i in range(4, 0, -1):
#     print(" " * (4 - i - 1) + "*", end="")
#     if i > 1:
#         print(" " * (2*i - 1) + "*", end="")
#     print()

# ********
# Upper half
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "*", end="")
    if i > 0:
        print(" " * (2*i - 1) + "*", end="")
    print()

# Lower half
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*", end="")
    if i > 0:
        print(" " * (2*i - 1) + "*", end="")
    print()