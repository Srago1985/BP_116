# part 1
def alex():
    return 4.5

def hanna():
    return 5.5

def zina():
    return 2.3

def haim():
    return 1.5

basket = 0
basket = basket + alex()
print(basket)
basket = basket + hanna()
print(basket)
basket = basket + zina()
print(basket)
basket = basket + haim()
print(basket)

average = basket / 4
print(f"{average:.2f}")

# part 2
def substract_100(value):
    return value - 100

print(f"{substract_100(25.7):.2f}")

# part 3
def calculate_percentage(value, percent):
    return value * (percent / 100)

print(f"{calculate_percentage(200, 15):.2f}")