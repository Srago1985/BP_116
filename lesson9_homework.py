# # part 1
def has_digit_count(number: int, digit: int):
    if digit < 0 or digit > 9:
        return "ERROR!"
    if number < 0:
        number = - number
    count = 0
    while number > 0:
        if number % 10 == digit:
            count += 1
        number //= 10
    return count

print(has_digit_count(123456759, 0))
print(has_digit_count(123456759, 5))
print(has_digit_count(-123456759, 3))
print(has_digit_count(123456759, -6))

# part 2 + part 4
def print_reverse_number(number: int):
    abs_number = abs(number)
    reversed_number = 0
    while abs_number > 0:
        reversed_number = reversed_number * 10 + abs_number % 10
        abs_number //= 10
    if number < 0:
        return -reversed_number
    return reversed_number
print(print_reverse_number(12345))
print(print_reverse_number(-67890)) # how to solve trouble with disappearing zeros without using str?
print(print_reverse_number(1000))

# part 3
def print_number_in_column(number: int):
    if number < 0:
        print("Number cannot be negative")
        return
    reversed_number = print_reverse_number(number) # reusing the previous function
    if reversed_number == 0:
        print(0)
        return
    while reversed_number > 0:
        print(reversed_number % 10)
        reversed_number //= 10
print_number_in_column(12345)