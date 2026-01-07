# basic.py

# Python List Overview
# A list is a built-in data structure that can hold an ordered collection of items.
# Key Features:
# - Can contain duplicate items
# - Mutable: items can be modified, replaced, or removed
# - Ordered: maintains the order of elements
# - Index-based access: items are accessed by their position
# - Can store mixed data types

# Creating a List
# 1. Using Square Brackets
a = [1, 2, 3, 4, 5]          # List of integers
b = ['apple', 'banana', 'cherry']   # List of strings
c = [1, 'hello', 3.14, True]  # Mixed data types

print(a)    # Output: [1, 2, 3, 4, 5]
print(b)    # Output: ['apple', 'banana', 'cherry']
print(c)    # Output: [1, 'hello', 3.14, True]

# 2. Using list() Constructor
a = list((1, 2, 3, 'apple', 4.5))
print(a)    # Output: [1, 2, 3, 'apple', 4.5]

b = list("GFG")
print(b)    # Output: ['G', 'F', 'G']

# 3. Creating List with Repeated Elements
a = [2] * 5
b = [0] * 7

print(a)    # Output: [2, 2, 2, 2, 2]
print(b)    # Output: [0, 0, 0, 0, 0, 0, 0]

# Accessing List Elements
a = [10, 20, 30, 40, 50]

print(a[0])    # Output: 10 (first element)
print(a[-1])   # Output: 50 (last element)
print(a[1:4])   # Output: [20, 30, 40] (elements from index 1 to 3)

# Adding Elements to a List
a = []

a.append(10)
print("After append(10):", a)    # Output: [10]

a.insert(0, 5)
print("After insert(0, 5):", a)    # Output: [5, 10]

a.extend([15, 20, 25])
print("After extend([15, 20, 25]):", a)    # Output: [5, 10, 15, 20, 25]

a.clear()
print("After clear():", a)    # Output: []

# Updating Elements in a List
a = [10, 20, 30, 40, 50]
a[1] = 25
print(a)    # Output: [10, 25, 30, 40, 50]

# Removing Elements from a List
a = [10, 20, 30, 40, 50]

a.remove(30)
print("After remove(30):", a)    # Output: [10, 20, 40, 50]

popped_val = a.pop(1)
print("Popped element:", popped_val)    # Output: 20
print("After pop(1):", a)    # Output: [10, 40, 50]

del a[0]
print("After del a[0]:", a)    # Output: [40, 50]

# Iterating Over Lists
a = ['apple', 'banana', 'cherry']
for item in a:
    print(item)
# Output:
# apple
# banana
# cherry

# Nested Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])    # Output: 6

# List Comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)    # Output: [1, 4, 9, 16, 25]

# How Python Stores List Elements
# Lists store references to objects, not the
