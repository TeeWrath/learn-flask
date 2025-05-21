# collect arguments
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total *= arg
    
    print(total)
    # return total
    
multiply(1,3,5)

# destructure arguments
def add(*args):
    total = 0
    for arg in args:
        total += arg
    print(total)
    
nums = [15,8]
add(*nums)

# for dictionaries
dictnum = {"x": 25, "y": 55}
add(**dictnum)
add(x=dictnum["x"], y=dictnum["y"])

# complex functions
def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return add(*args)
    else:
        return "No valid operator provided"

apply(1,3,4,5,6,10, operator="+")
apply(2,3,8,2,operator="*")