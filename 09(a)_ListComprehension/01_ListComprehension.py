# List Comprehensions in Python
'''
# Cleaner Code: Do the same work in one line instead of long loops.
# Better Performance: Faster than normal for loops in most cases.
# Filter + Change Together: Select and modify items in one step.
# Easy to Read: Looks clean, Pythonic, and easy to understand.
'''

# 1. Basic List Comprehension
# Create a list of squares for numbers from 0 to 4
squares = [x ** 2 for x in range(5)]
print("List of squares:", squares)

# 2. Filtering with List Comprehensions
# Create a list of even numbers from 0 to 9
evens = [x for x in range(10) if x % 2 == 0]
print("List of even numbers:", evens)

# 3. Nested List Comprehensions
# Create a list of pairs (i, j) for i and j in range(3)
pairs = [(i, j) for i in range(3) for j in range(3)]
print("List of pairs:", pairs)

# 4. List Comprehensions vs. Regular Loops
# Using a loop to create the same list of squares
squares_loop = []
for x in range(5):
    squares_loop.append(x ** 2)
print("List of squares using loop:", squares_loop)

# Note: List comprehensions are generally more concise and often more efficient than using loops.

# 5. Performance Note
# List comprehensions are generally faster than equivalent for-loops due to optimization in Python’s implementation.
