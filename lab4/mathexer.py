#1
import math

degree = float(input("Input degree: "))
radian = math.radians(degree)
print("Output radian:", radian)

#2
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))
area = 0.5 * (base1 + base2) * height
print("Expected Output:", area)

#3
num_sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))
area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))
print("The area of the polygon is:", area)

#4
base_length = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area = base_length * height
print("Expected Output:", area)

