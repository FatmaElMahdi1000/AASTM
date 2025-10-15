def selected_colors(color_list):
    length = len(color_list)
    for i in range(0, length):
        return "First Color: " + color_list[i], "Second Color: ", color_list[i-1]

color_list = ["Red", "Green", "White", "Black"]
selected = selected_colors(color_list)
print(selected)