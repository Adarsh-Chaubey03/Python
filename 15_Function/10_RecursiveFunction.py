# Create a recursive function to calculate factorial
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

print(fact(5))

# Fibonnacci

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
