#Nirmiti bhopi B51
import math
print("Area Calculator")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = int(input("Enter your choice (1-3): "))
if choice == 1:
    radius = float(input("Enter radius of the circle: "))
    area = math.pi * radius * radius
    print("Area of Circle =", area)
elif choice == 2:
    length = float(input("Enter length of the rectangle: "))
    breadth = float(input("Enter breadth of the rectangle: "))
    area = length * breadth
    print("Area of Rectangle =", area)
    
elif choice == 3:
    base = float(input("Enter base of the triangle: "))
    height = float(input("Enter height of the triangle: "))
    area = 0.5 * base * height
    print("Area of Triangle =", area)

else:
    print("Invalid choice")
