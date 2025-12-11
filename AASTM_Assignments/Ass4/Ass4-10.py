#2 is the only even prime number, every other prime number is odd, divided by 1 and itself
num = int(input("Enter a number: "))
if num <= 1:
    print(f"{num} is not a prime number!")

else:
    for n in range(2, num):
        if num % n == 0:
            print(f"{num} is not a prime number!")
            break #preventing form going through the remaining list of Nums
    else: #if for ran (went through all iterations without breaking, checking its condition),
        print(f"{num} is a prime number!")
