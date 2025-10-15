def circle_area(pi, radius):
    return pi * radius ** 2 #circle area

pi = 3.14
radius = float(input("Enter the radius of the circle: "))
Circle_Area = circle_area(pi, radius)
print(Circle_Area)