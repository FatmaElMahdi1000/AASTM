def Reverse(Name):
    return Name[::-1]

Name = input("Enter your Name: ")
Reversed = Reverse(Name)
print(Reversed)
print("********------ANOTHER WAY!-----***************")
def Reverse(Name):
    Reversed_Name = ""
    for char in Name:
        Reversed_Name = char + Reversed_Name
    return Reversed_Name

Name = input("Enter your Name: ")
print(Reverse(Name))