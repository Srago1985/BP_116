# part1
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

def addition(a, b):
    return a + b

result = addition(a, b)
print(f"The result of the addition is: {result:.2f}")

# part2
c = float(input("Enter the first number: "))
d = float(input("Enter the second number: "))

def division(c, d):
    if d == 0:
        return "Error: Division by zero is not allowed."
    return c / d

result = division(c, d)
print(f"The result of the division is: {result:.2f}" if isinstance(result, float) else result)

# part3

def calculate_salary (hours, wage, bonus, tax, insurance, pension, education):
    basic_salary = hours * wage
    gross_salary = basic_salary + (basic_salary * bonus / 100)
    deductions = (gross_salary * tax / 100) + (gross_salary * insurance / 100) + (gross_salary * pension / 100) + (gross_salary * education / 100)
    net_salary = gross_salary - deductions

    return net_salary

h = float(input("Enter the number of hours worked: "))
w = float(input("Enter the hourly wage: "))
b = float(input("Enter the bonus (percentage): "))
t = float(input("Enter the tax (percentage): "))
i = float(input("Enter the insurance (percentage): "))
p = float(input("Enter the pension contribution (percentage): "))
e = float(input("Enter the education contribution (percentage): "))

net_salary = calculate_salary(h, w, b, t, i, p, e)
print(f"The net salary is: {net_salary:.2f}")