import math

num_list = []
i = 1
while i <= 4:
    num = int(input("Enter a number: "))
    num_list.append(num)
    i += 1
sorted_list = sorted(num_list)

length = len(sorted_list)

if length % 2 != 0:
    Median = sorted_list[length // 2]
    print(f"Median is : {Median}")
else:
    num1 = sorted_list[(length//2)]
    num2 = sorted_list[(length//2) - 1]
    Median = (num1+num2) / 2
    print(f"Median is : {Median}")


