def fizzbuzz(num_list):
    updated_list = []
    for num in num_list:
        if num % 3 == 0:
            updated_list.append("Fizz")
        elif num % 5 == 0:
            updated_list.append("Buzz")
        elif num % 3 == 0 and num % 5 == 0:
            updated_list.append("Buzz")
        else:
            updated_list.append(num)
    return updated_list

num_list = [num for num in range(1, 51)]
Result = fizzbuzz(num_list)
print(Result)