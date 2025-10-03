"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""

def add(a, b):
    """Add two numbers together"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b): 
    """Raise a to the power of b""" 
    return a ** b 

def square_root(a): 
    """Calculate square root of a""" 
    if a < 0: 
        raise ValueError("Cannot calculate square root of negative number") 
    return a ** 0.5

# TODO: Students will add multiply, divide, power, sqrt functions

if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")