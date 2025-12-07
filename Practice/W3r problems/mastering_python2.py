List_A = list(range(0, 10))

odd_numbers = [n for n in List_A if n %2 != 0]
print(odd_numbers)
odd_and_others = [-1 if n %2 != 0 else n for n in List_A  ]
print(odd_and_others)

lst = [-1, 2, 0, -4, 5]
updated = [True if n != 0 else n for n in lst]
print(updated)

updated = [True if n != 0 else False for n in lst]
print(updated)
updated = [bool(n) for n in lst]
print(updated)