def documentation(func):
    return abs.__doc__

num = 5
func = abs(num)
result = documentation(func)
print(result)