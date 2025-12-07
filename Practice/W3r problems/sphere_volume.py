import math
def sphere_volume(r):
    return (4/3) * math.pi * math.pow(r, 3)

r = int(input("Enter the radius: "))
result = sphere_volume(r)
print(result)






