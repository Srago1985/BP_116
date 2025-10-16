def solution(string):
    return string[::-1]

print(solution("world"))  # "dlrow"

def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    array = []
    i = 1
    while i <= n:
        array.append(x * i)
        i += 1
    return array

def boolean_to_string(b: bool) -> str:
    return "True" if b else "False"

def check(seq, elem):
    return elem in seq

def simple_multiplication(number) :
    # Your code goes here
    return number * 8 if number % 2 == 0 else number * 9

def dna_to_rna(dna):
    rna = dna
    for i in rna:
        if i == "T":
            i = "U"
    return rna

print(dna_to_rna("GCAT"))  # Output: "GCAU"

def grow(arr):
    import math
    return math.prod(arr) if arr else 0


def count_sheep(n):
    # your code
    if n == 0:
        return
    i = 1
    sheeps = ""
    while i <= n:
        sheeps = sheeps + (str(i) + " sheep...")
        i += 1
    return sheeps
print(count_sheep(3))  # Output: "1 sheep...2 sheep...3 sheep..."

def disemvowels(string_):
    vowels = "aeiouAEIOU"
    for i in string_:
        if i in vowels:
            string_ = string_.replace(i, "")
    return string_

def square_digits(num):
    return int(''.join(str(int(i) ** 2) for i in str(num)))

def nb_year(p0, percent, aug, p):
    # your code
    years = 0
    while p0 < p:
        p0 = int(p0 * (1 + percent/100) + aug)
        years += 1
    return years