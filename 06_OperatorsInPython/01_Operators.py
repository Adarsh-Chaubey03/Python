
# Addition
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8



# Subtraction
def subtract(a, b):
    return a - b

result = subtract(5, 3)
print(result)  # Output: 2



# Multiplication
def multiply(a, b):
    return a * b

result = multiply(5, 3)
print(result)  # Output: 15



# Division
def divide(a, b):
    """Returns the quotient of a divided by b. Raises an error if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

result = divide(6, 3)
print(result)  # Output: 2.0



# Modulo
def modulo(a, b):
    """Returns the remainder of a divided by b."""
    return a % b

result = modulo(5, 3)
print(result)  # Output: 2




# Exponentiation
def power(a, b):
    """Returns a raised to the power of b."""
    return a ** b

result = power(2, 3)
print(result)  # Output: 8


# Square root
import math

def sqrt(a):
    """Returns the square root of a."""
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(a)

result = sqrt(9)
print(result)  # Output: 3.0
