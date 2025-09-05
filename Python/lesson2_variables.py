# types of variables in Python: int, float, str, bool
# type of variable changes dynamically

variable = 5
print("type(variable):", type(variable)) # "type" gives the type of the variable
print(f"variable = {variable}")
print("variable =", variable)

year = input("Enter your year of birth→")
print("year:", year)
# "input" always returns a string, so we need to convert it to an integer
age = 2025 - int(year)
print("age:", age)