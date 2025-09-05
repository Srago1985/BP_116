# part 1
def find_min_value(arr):
    min_value = arr[0]
    for num in arr:
        if num < min_value:
            min_value = num
    return min_value

# part 2
def sum_odds_positives(arr):
    total = 0
    for num in arr:
        if num % 2 != 0 and num > 0:
            total += num
            if total == 0:
                return "Нет нечетных положительных чисел"
    return total

# part 3
def find_max_even_value(arr):
    max_even_value = None # Инициализация пустой переменной
    for num in arr:
        if num % 2 == 0:
            if max_even_value is None or num > max_even_value:
                max_even_value = num
    if max_even_value is None:
        return "Нет четных чисел"
    return max_even_value

# part 4
def find_min_positive_value(arr):
    min_positive = None
    for num in arr:
        if num > 0:
            if min_positive is None or num < min_positive:
                min_positive = num
    if min_positive is None:
        return "Нет положительных чисел"
    return min_positive
arr = [-3, 5, 1, -7, -6, 4, 9]
print(find_min_value(arr))
print(sum_odds_positives(arr))
print(find_max_even_value(arr))
print(find_min_positive_value(arr))