# Syntax 
# def function_name(parameters):
#     """Docstring"""
#     # function body
#     return expression

def even_or_odd(num):
    """This function finds even or odd"""
    if num%2==0:
        print("the number is even")
    else:
        print("the number is odd")

# call the function
even_or_odd(34)

# Default parameters
def greet(name="John"):
    print(f"Hello {name}, welcome to the paradise.")

greet()

## Variable length arguments
## Positional and Keywords arguments

# positional args
def print_element(*elements):
    for element in elements:
        print(element)

print_element(1,2,2,"string",False)

# keyword args => works for key, value pair args
def print_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_details(name="John",age="16",country="USA")

# keywords and positional together
def print_all(*args,**kwargs):
    for val in args:
        print(f"Positional args: {val}")

    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_all(1,2,3,"hi",name="John",age="16",country="USA")