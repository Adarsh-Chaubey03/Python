# basic.py

# Dictionary in Python
# A dictionary is a data structure that stores values in key: value pairs.
# Keys must be immutable and unique, and values can be of any data type.

# Creating a Dictionary
d1 = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d1)  # Output: {1: 'Geeks', 2: 'For', 3: 'Geeks'}

# Using dict() constructor
d2 = dict(a="Geeks", b="for", c="Geeks")
print(d2)  # Output: {'a': 'Geeks', 'b': 'for', 'c': 'Geeks'}

# Accessing Dictionary Items
d = {"name": "Prajjwal", 1: "Python", (1, 2): [1, 2, 4]}
print(d["name"])  # Output: Prajjwal
print(d.get("name"))  # Output: Prajjwal

# Adding and Updating Dictionary Items
d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
d["age"] = 22  # Adding new key-value pair
d[1] = "Python dict"  # Updating existing key
print(d)  # Output: {1: 'Python dict', 2: 'For', 3: 'Geeks', 'age': 22}

# Removing Dictionary Items
d = {1: 'Geeks', 2: 'For', 3: 'Geeks', 'age': 22}
del d["age"]  # Remove by key
print(d)  # Output: {1: 'Geeks', 2: 'For', 3: 'Geeks'}

val = d.pop(1)  # Remove and return value by key
print(val)  # Output: Geeks

key, val = d.popitem()  # Remove and return last key-value pair
print(f"Key: {key}, Value: {val}")  # Output: Key: 3, Value: Geeks

d.clear()  # Clear all items
print(d)  # Output: {}

# Iterating Through a Dictionary
d = {1: 'Geeks', 2: 'For', 'age': 22}

# Iterate over keys
for key in d:
    print(key)  # Output: 1, 2, 'age'

# Iterate over values
for value in d.values():
    print(value)  # Output: Geeks, For, 22

# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")  # Output: 1: Geeks, 2: For, age: 22

# Nested Dictionaries
d = {1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
print(d)  # Output: {1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
