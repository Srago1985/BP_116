# def verni_sotku():
#     return 100

# pocket = verni_sotku()

# print(pocket)

# pocket = pocket + verni_sotku()

# print(pocket)


def ilya():
    return 100


def hanna():
    return 150.50

def anton():
    return 35.50

def vika():
    return 500.75


wallet = ilya() + hanna() + anton() + vika()
print(wallet)

average = wallet / 4
print(f"{average:.2f}")


def let_double_with_param(value):
    doubled_value = value * 2
    return doubled_value

print(f"{let_double_with_param(5):.2f}")


def divide_on_3(value):
    return value / 3

result = divide_on_3(80)
print(f"{result:.2f}")


def sum_of_two_numbers(a, b):
    return a + b

result = sum_of_two_numbers(5, 10)
print(f"{result:.2f}")