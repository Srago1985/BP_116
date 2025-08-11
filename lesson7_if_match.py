def my_number(number):
    if number < 0:
        print("Negative number")
    elif number > 0:
        print("Positive number")
    else:
        print("Zero")
        
def is_even_or_odd(number):
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
        
        
def calculator(a, operation, b):
    result = 0
    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        if b != 0:
            result = a / b
        else:
            return "Cannot divide by zero"
    elif operation == "**":
        result = a ** b
    else:
        return "Invalid operation"
    return result

res = calculator(10, "beer", 0)
if isinstance(res, str):
    print(res)
else: 
    print(f"Result of the operation: {res:.2f}")

