def Fib(Fib_sequence):
    # Base case: stop if next Fibonacci number would exceed 50
    if Fib_sequence[-2] + Fib_sequence[-1] > 50:
        return Fib_sequence

    else:
        New_num = Fib_sequence[-1] + Fib_sequence[-2]
        Fib_sequence.append(New_num)
        return Fib(Fib_sequence)

Fib_sequence = [0, 1]
result = Fib(Fib_sequence)
print(result)