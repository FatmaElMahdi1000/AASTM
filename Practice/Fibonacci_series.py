# def Fib(Fib_sequence):
#     # Base case: stop if next Fibonacci number would exceed 50
#     if Fib_sequence[-2] + Fib_sequence[-1] > 50:
#         return Fib_sequence
#
#     else:
#         New_num = Fib_sequence[-1] + Fib_sequence[-2]
#         Fib_sequence.append(New_num)
#         return Fib(Fib_sequence)
#
# Fib_sequence = [0, 1]
# result = Fib(Fib_sequence)
# print(result)

##########################
# fib_list = [0, 1, 1]
#
# while True:
#     new_num = fib_list[-1] + fib_list[-2]
#     if new_num > 50:
#         break
#     else:
#         fib_list.append(new_num)
# print(fib_list)
##########################
fib = [0, 1, 1]
for n in range(2, 15):
    fib_num = fib[-1] + fib[-2]
    fib.append(fib_num)
print(fib)









