my_numbers = [1, 2, 3, 4, 5]
print(my_numbers)
print(type(my_numbers))
print(len(my_numbers))

my_numbers[2] = 10
print(my_numbers)
my_numbers[3] = my_numbers[3] * 10
print(my_numbers)

my_teams = ["Real", "Barca", "Bayern", "Juventus"]
print(my_teams)
for team in my_teams:
    team = team.upper()
    print(team, end=" ")
    
print()

count = 0
while count < len(my_teams):
    my_teams[count] = my_teams[count].upper()
    count += 1

print(my_teams)

arr1 = [1, "beer", 3.5, True]
print(arr1)

def sum_numbers_in_array(arr:list):
    total = 0
    for a in arr:
        total += a
    return total

print(sum_numbers_in_array(my_numbers))

arr2 = [10, 20, 30, 40, 13]
arr3 = [100, 200, 300]
def print_array_reverse_in_row(arr:list):
    index = len(arr) - 1
    while index >= 0:
        print(arr[index], end=" ")
        index -= 1
    print()
print_array_reverse_in_row(arr2)
print_array_reverse_in_row(arr3)

def array_mult_10(arr:list):
    count = 0
    while count < len(arr):
        arr[count] *= 10
        count += 1
    return arr
print(array_mult_10(arr2))
print(array_mult_10(arr3))

del arr3[1]
print(arr3) 

arr1 = [1, 1, 2, 3, 5, 8, 13, 21]
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def is_arrays_equal(arrA:list, arrB:list):
    if len(arrA) != len(arrB):
        return False
    for i in range(len(arrA)):
        if arrA[i] != arrB[i]:
            return False
    return True