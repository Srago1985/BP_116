# part 1
def factorial(n: int):
    result = 1
    if n < 0:
        return "Factorial is not defined for negative numbers"
    while n > 1:
        result *= n
        n -= 1
    return result

print(factorial(-1))
print(factorial(5))
print(factorial(0))

# part 2
def print_stars(n: int):
    if n < 0:
        print("Number of stars cannot be negative")
    elif n == 0:
        print("No stars to print")
    while n > 0:
        print("*", end="")
        n -= 1
    print()  # Move to the next line after printing all stars
print_stars(5)
print_stars(0)
print_stars(-3)

# part 3
def x_power_y(x: float, y: int):
    if y < 0:
        return "Exponent cannot be negative"
    result = 1
    while y > 0:
        result *= x
        y -= 1
    return result
print(x_power_y(2, 3))  
print(x_power_y(5, 0))  
print(x_power_y(2, -3))  