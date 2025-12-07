def triangle_checker(side1, side2, side3):
    if  side1 == side2 == side3:
        return "The triangle is equilateral!"
    elif (side1 == side3) or (side1 == side2) or (side1 == side3) or (side2 == side3):
        return "The triangle is isosceles!"
    else:
        return "The triangle is scalene!"

while True:
    side1 = input("Enter triangle side1: ").strip()
    side2 = input("Enter triangle side2: ").strip()
    side3 = input("Enter triangle side3: ").strip()
    if side1.isdigit() and side2.isdigit() and side3.isdigit():
        side1 = int(side1)
        side2 = int(side2)
        side3 = int(side3)
        break
    else:
        print("invalid inputs, Enter a digit!")
        continue  # ignore the following lines and start over the while loop, prompting the user for new inputs.

checking_Result = triangle_checker(side1, side2, side3)
print(checking_Result)
