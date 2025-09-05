# part 1

def print_string_in_column(myStr:str):
    for i in myStr:
        print(i)
        
print_string_in_column("Hello")

# part 2
def return_string_reverse_upped(myStr:str):
    upper_str = myStr.upper()
    while len(upper_str) > 0:
        print(upper_str[-1], end="")
        upper_str = upper_str[:-1]
    return upper_str
return_string_reverse_upped("Hello")
print()  # For newline

# part 3
def is_subnumber_in_number(number:int, subnumber:int):
# without converting to string
    number = abs(number)
    subnumber = abs(subnumber)
    if subnumber == number:
        return True
    if subnumber > number:
        return False
    if 0 <= subnumber < 10:
        while number > 0:
            if number % 10 == subnumber:
                return True
            number //= 10
        return False
    else:
        subnumber_length = 0
        temp_subnumber = subnumber
        while temp_subnumber > 0:
            subnumber_length += 1
            temp_subnumber //= 10
        divisor = 10 ** subnumber_length
        while number >= subnumber:
            if number % divisor == subnumber:
                return True
            number //= 10
        return False

# with converting to string
def is_subnumber_in_number_v2(number:int, subnumber:int):
    return str(subnumber) in str(number)
