def count(num_list):
    odd_num = []
    even_num = []
    for n in num_list:
        if n % 2 == 0:
            even_num.append(n)
        else:
            odd_num.append(n)
    return "Odd numbers are: ", odd_num, "Even numbers are: ", even_num

num_list = []
list_length = 10
i = 0
while i <= list_length:
    num = input("Enter a number: ").strip() #removes any trailing spaces or leading spaces
    if not num.strip():
        num = input("invalid num, re-enter: ")
    else:
        num_list.append(int(num))
    i += 1
result = count(num_list)
print(result)