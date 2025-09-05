# part 1
def change(total, cash, discount):
    change = cash - (total - (discount/100 * total))
    return change

change = change(100, 120, 10)
print(f"Change to be returned: {change}")

# part 2
def fan(mode: int):
    if mode == 0:
        print("switched off")
    elif mode == 1:
        print("speed 1")
    elif mode == 2:
        print("speed 2")
    elif mode == 3:
        print("turbo mode")
    else:
        print("fan is breaking down")

fan(0)
fan(1)
fan(2)
fan(3)
fan(4)

# part 3
def my_age (age: int):
    if age < 0:
        print("Age cannot be negative.")
    elif age < 18:
        print("You are a child.")
    elif 18 <= age < 65:
        print("You are an adult.")
    else:
        print("You are a senior.")
        
my_age(15)
my_age(25)
my_age(70)