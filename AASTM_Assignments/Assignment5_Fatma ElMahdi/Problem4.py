G1 = []
G2 = []
st_G1 = int(input("Enter the number of the students registered in G1: "))
print("Please Enter their marks:")
for x in range(1, st_G1+1):
    mark_G1 = int(input(f"Student ({x}): "))
    G1.append(mark_G1)

st_G2 = int(input("Enter the number of the students registered in G2: "))
print("Please Enter their marks:")
for s in range(1, st_G2+1):
    mark_G2 = int(input(f"Student ({s}): "))
    G2.append(mark_G2)

print(f"The concatenated grades: {G1+G2}")