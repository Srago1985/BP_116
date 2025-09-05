str1 = "Hello"
print(str1)

number = 10
str2 = str(number)
print(str2, type(str2))

num1 = 22
num2 = 33
str3 = str(num1)
str4 = str(num2)
print(str3 + str4)  # Concatenation 
print(str1 * 3)  # Repetition 

length = len(str1) # Get length of string
print(length)

a = str1[0]  # First character
b = str1[1]  # Second character
c = str1[2]  # Third character
print(a, b, c)

def print_str_reverse(str1):
    while len(str1) > 0:
        print(str1[-1], end="")
        str1 = str1[:-1]
    
print_str_reverse(str1)
print()  # For newline

str1 = -12300
str1 = str(str1)
print_str_reverse(str1)
print()  # For newline

str1 = "Hello, World!"
for i in str1:
    print(i, end="")
print()  # For newline

substr = "Hello"
print(substr in str1)  # Check substring presence
print(substr not in str1)  # Check substring absence
print(str1.upper()) # Convert to uppercase
print(str1.lower()) # Convert to lowercase
print(str1.replace("World", "Python")) # Replace substring
print(str1.split(" ")) # Split string by delimiter