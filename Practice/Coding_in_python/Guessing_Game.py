def guessing(num):
    while True:
        if num in range(1, 11):
            return "Your Guess is correct, Number is within the range"
        else:
            print("Out of range! Try again.")
            num = int(input("Guess a num: "))

num = int(input("Guess a num: "))
Result = guessing(num)
print(Result)