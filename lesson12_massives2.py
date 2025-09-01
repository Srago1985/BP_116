arr = [-3, 5, 1, -7, -6, 4, 9]
arr.sort()
print(arr[len(arr)-1])  # максимальный элемент

def find_max_value(arr):
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value

print(find_max_value(arr))

def find_min_even_value(arr):
    min_even_value = None
    for num in arr:
        if num % 2 == 0:
            if min_even_value is None or num < min_even_value:
                min_even_value = num
    if min_even_value is not None:
        return min_even_value
    return "Нет четных чисел"

print(find_min_even_value(arr))

def sum_evens_negatives(arr):
    total = 0
    for num in arr:
        if num % 2 == 0 and num < 0:
            total += num
    if total == 0:
        return "Нет четных отрицательных чисел"
    return total

print(sum_evens_negatives(arr))