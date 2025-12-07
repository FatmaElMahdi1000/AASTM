def guess_num(target):
    while True:
        try:  #Keep trying entering a value till it's a number
            Guess = int(input("Enter a guess: "))
            if Guess in target and isinstance(Guess, int):
                return "Well guessed!"
            else:
                print("Wrong Answer!")
        except ValueError:
            print("Invalid input! Please enter a number.")

target = [num for num in range(1, 10)]
Result = guess_num(target)
print(Result)