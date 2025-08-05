# part1
def addition(a, b):
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    return a + b

result = addition(0, 0)
print(f"The result of the addition is: {result:.2f}")

# part2
def division(a, b):
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

result = division(0, 0)
print(f"The result of the division is: {result:.2f}" if isinstance(result, float) else result)

# part3
def calculate_salary (hours, wage, bonus, tax, insurance, pension, education):
    hours = float(input("Enter the number of hours worked: "))
    wage = float(input("Enter the hourly wage: "))
    bonus = float(input("Enter the bonus (percentage): "))
    tax = float(input("Enter the tax (percentage): "))
    insurance = float(input("Enter the insurance (percentage): "))
    pension = float(input("Enter the pension contribution (percentage): "))
    education = float(input("Enter the education contribution (percentage): "))

    basic_salary = hours * wage
    gross_salary = basic_salary + (basic_salary * bonus / 100)
    deductions = (gross_salary * tax / 100) + (gross_salary * insurance / 100) + (gross_salary * pension / 100) + (gross_salary * education / 100)
    net_salary = gross_salary - deductions

    return net_salary
net_salary = calculate_salary(0, 0, 0, 0, 0, 0, 0)
print(f"The net salary is: {net_salary:.2f}")