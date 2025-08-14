def fan(mode: int):
    match mode:
        case 0:
            return "Fan is off"
        case 1:
            return "Fan is on low speed"
        case 2:
            return "Fan is on medium speed"
        case 3:
            return "Fan is on high speed"
        case _: # default case (if no match found)
            return "Invalid mode"
        
def calculator(a: float, operation: str, b: float):
    res = 0
    match operation:
        case "+":
            res = a + b
        case "-":
            res = a - b
        case "*":
            res = a * b
        case "/":
            if b == 0:
                return "Cannot divide by zero"
            res = a / b
        case _:
            return "Invalid operation"
    return res