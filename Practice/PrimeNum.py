num = int(input("Enter the number: "))
#
# if num == 2:
#     print(f"the {num} is a prime")
# elif num > 1:
#     for n in range(2, num):
#         if num % n == 0:
#             print(f"the {num} is not a prime")
#             break
#     else:
#         print(f"the {num} is a prime")
status = True
for i in range(2, num):
    if num%i == 0: #not a prime
        status = False
        print(f"{num} is not a prime number")
        break
if status == True and num != 1:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")




