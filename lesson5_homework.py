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
hours = float(input("Enter the number of hours worked: "))
wage = float(input("Enter the hourly wage: "))
bonus = float(input("Enter the bonus (percentage): "))
tax = float(input("Enter the tax (percentage): "))
insurance = float(input("Enter the insurance (percentage): "))
pension = float(input("Enter the pension contribution (percentage): "))
education = float(input("Enter the education contribution (percentage): "))

def calculate_salary (hours, wage, bonus, tax, insurance, pension, education):
    basic_salary = hours * wage
    gross_salary = basic_salary + (basic_salary * bonus / 100)
    deductions = (gross_salary * tax / 100) + (gross_salary * insurance / 100) + (gross_salary * pension / 100) + (gross_salary * education / 100)
    net_salary = gross_salary - deductions

    return net_salary
net_salary = calculate_salary(hours, wage, bonus, tax, insurance, pension, education)
print(f"The net salary is: {net_salary:.2f}")