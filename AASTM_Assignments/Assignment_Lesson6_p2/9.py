Grades = [("Omar",40,20,40),("Soha",35,15,30),("Amir",38,14,33),("Nada",10,10,10),("Ingy",25,18,27)]

print("Name\t\t7th\t\tAtt\t\tFinal")
for i in range(len(Grades)):
    for j in range(len(Grades[i])):
        print(Grades[i][j], end="\t\t")
    print()

