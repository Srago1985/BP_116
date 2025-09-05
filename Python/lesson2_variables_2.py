# number1 = input("Enter the first number→")
# number2 = input("Enter the second number→")
# sum = float(number1) + float(number2)
# print("The sum is", sum)
# print(f"The sum is {sum:.2f}")

# hours = float(input("Enter hours worked→"))
# wage = float(input("Enter hourly wage→"))
# salary = hours * wage
# print(f"The salary is {salary:.2f} NIS")

radius = float(input("Enter the radius of the circle→"))
import math
area = math.pi * radius ** 2  # area = π * r^2
print(f"The area of the circle is {area:.2f} square units")
volume = (4/3) * math.pi * radius ** 3  # volume = (4/3) * π * r^3
print(f"The volume of the sphere is {volume:.2f} cubic units")