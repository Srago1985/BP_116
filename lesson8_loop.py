
# barrel = 0

# while barrel < 100:
#     barrel += 10
#     print(f"Barrel filled to {barrel} liters")
# print("Barrel is full!")

def number_sum(n: int):
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total

print(number_sum(5))  # Output: 15