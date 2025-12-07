def find_lineup(distances):
    original_line = []
    distances_set = set(distances)
    if len(distances_set) != len(distances) or len(distances) == 1 :
        return []
    if len(distances_set) == 0:
        return [1]

    for i in range(0, len(distances)):
        diff = distances[i]
        original_line.insert(diff, i+1)
    return original_line


distances = [1, 2, 0]
result = find_lineup(distances)
print(result)
