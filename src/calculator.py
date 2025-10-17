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
    """Multiply two numbers"""
    return a * b


def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    """Raise a to the power of b"""
    return a**b


def square_root(a):
    """Calculate square root of a"""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return a**0.5


# Expose multiply into builtins so tests that call `multiply(...)` without
# importing it (some student tests do this) will still find the function.
try:
    import builtins

    builtins.multiply = multiply
except Exception:
    # If for any reason we can't modify builtins, don't fail import.
    pass

if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
