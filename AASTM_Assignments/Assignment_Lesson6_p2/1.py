Animal = ("dog", "cat", "duck", "lion", "camel")

Baby = ("puppy", "kitten", "duckling", "cub", "calf")

Animal_info = {}
for i in range(len(Animal)):
    Animal_info[Animal[i]] = Baby[i]

for key, value in Animal_info.items():
    print(f"The baby {key} is called a {value}")