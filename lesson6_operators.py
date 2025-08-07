a = 14
b = 3
result = a % b #1 % returns the remainder of the division of a by b
print(f"The result of {a} % {b} is: {result}")

result2 = a // b #2 // returns the integer division of a by b
print(f"The result of {a} // {b} is: {result2}")

a = 5
b = 5
res = a > b
print(f"The result of {a} > {b} is: {res}")

result = a > 0 or b == a
print(f"The result of {a} > 0 or {b} == {a} is: {result}")

if a > 0 and b == a:
    print(f"{a} is greater than 0 and {b} is equal to {a}")
else:
    print(f"{a} is not greater than 0 or {b} is not equal to {a}")
    
    
def taxi(name):
    if name == "Alex":
        print("Alex, go!")
    if name == "John":
        print("John, go!")
    if name == "Mike":
        print("Mike, go!")
    if name not in ["Alex", "John", "Mike"]:
        print("You are not in the list of drivers, sorry!")
        
def divide(a, b):
    if b == 0:
        print("Division by zero is not allowed.")
    else:
        result = a / b
        print(f"The result of {a} / {b} is: {result:.2f}")

first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))

divide(first, second)