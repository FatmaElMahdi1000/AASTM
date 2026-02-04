import pandas as pd
# arr = [["Fatma", 29, "CS"], ["Basma", 22, "Engineering"]]
# data = pd.DataFrame(arr, columns=['Name', 'Age', 'faculty'])
# print(data)
#
# Dict_data = {}

# fruits = [
#     ["Apple", 1.23],
#     ["Banana", 2.2],
#     ["Cherry", 3.1]
# ]
# data = pd.DataFrame(fruits, columns=["Fruits", "Price"])
# data.index = data.index + 1
# print(data)


data  = {"Fruits": ["Apple", "Banana", "Cherry"], "Price": [1.2, 3.4, 4]}
df = pd.DataFrame(data, columns=["Fruits", "Price"])
df.index = df.index + 1
print(df)












