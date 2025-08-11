# part 1
def taxi(name):
    if name == "Alex":
        print("Alex, go!")
    elif name == "John":
        print("John, go!")
    elif name == "Mike":
        print("Mike, go!")
    else:
        print("You are not in the list of drivers, sorry!")
        
taxi("Alex")
taxi("John")
taxi("Mike")
taxi("Sarah")

# part 2
def is_alcohol_permit(age: int):
    if 0 <= age <= 17:
        print("Not permit")
    elif 18 <= age <= 75:
        print("Permit")
    elif 75 < age <= 150:
        print("Permit, but not recommended")

is_alcohol_permit(2)
is_alcohol_permit(18)
is_alcohol_permit(80)
        
# part 3
def time_to_work (hours: int, minutes: int):
    time_in_minutes = (hours * 60) + minutes
    time_float = time_in_minutes / 60
    if 6.5 <= time_float <= 8.5:
        return "34 minutes"
    elif 8.5 < time_float <= 9.5:
        return "47 minutes"
    elif 9.5 < time_float <= 11.5:
        return "36 minutes"
    else:
        return "ERROR!"

print(time_to_work(8, 30))