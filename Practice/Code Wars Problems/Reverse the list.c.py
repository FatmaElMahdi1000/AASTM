def reverse_list(l):
    l.sort(reverse=True)
    return l


l = [1, 2, 5, 6]
print(reverse_list(l))