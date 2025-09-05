str = "Hello, World!"
print(str[0], str[7])

i = len(str) - 1
while i >= 0:
    print(str[i], end="")
    i -= 1
    
print()

human = {"name": "John", "age": 23, "city": "New York"}
print(human["name"])

class Person:
    pass 
p = Person()
p.name = "Alice"
p.age = 30
p.city = "Los Angeles"

p1 = Person()
p1.name = "Bob"
p1.age = 25
p1.city = "Chicago"

p2 = Person()
p2.name = "Charlie"
p2.age = 28
p2.city = "San Francisco"

company = [p, p1, p2]

for person in company:
    print(f"{person.name} is {person.age} years old and lives in {person.city}.")