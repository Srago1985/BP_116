# part 1
def product_array_elements(arr: list):
    product = 1
    for num in arr:
        product *= num
    return product
print(product_array_elements([1, 2, 3, 4]))  # Output: 24


# part 2
def print_negative_elements_in_column(arr: list):
    for num in arr:
        if num < 0:
            print(num)
print_negative_elements_in_column([10, -5, 3, -1, 0, -7])  # Output: -5, -1, -7 

# part 3
def count_positive_elements(arr: list):
    count = 0
    for num in arr:
        if num >= 0:
            count += 1
    return count
print(count_positive_elements([-10, 5, 3, -1, 0, 7]))  # Output: 4

# part 4
def reverse_array(arr: list):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
print(reverse_array([1, True, 3, "beer", 5, -3.78]))  # Output: [-3.78, 5, "beer", 3, True, 1]

