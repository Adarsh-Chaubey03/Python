# basic.py

# Tuple in Python
# A tuple is an immutable ordered collection of elements.
# Tuples are similar to lists but cannot be changed after creation.
# They can hold elements of different data types.

# Creating a Tuple
tup = ()  # Empty tuple
print(tup)  # Output: ()

# Using parentheses with elements
tup = ('Geeks', 'For')
print(tup)  # Output: ('Geeks', 'For')

# Converting a list to a tuple
li = [1, 2, 4, 5, 6]
print(tuple(li))  # Output: (1, 2, 4, 5, 6)

# Using the tuple() constructor with a string
tup = tuple('Geeks')
print(tup)  # Output: ('G', 'e', 'e', 'k', 's')

# Creating a Tuple with Mixed Datatypes
tup = (5, 'Welcome', 7, 'Geeks')
print(tup)  # Output: (5, 'Welcome', 7, 'Geeks')

# Nested Tuples
tup1 = (0, 1, 2, 3)
tup2 = ('python', 'geek')
tup3 = (tup1, tup2)
print(tup3)  # Output: ((0, 1, 2, 3), ('python', 'geek'))

# Tuple Repetition
tup1 = ('Geeks',) * 3
print(tup1)  # Output: ('Geeks', 'Geeks', 'Geeks')

# Accessing Tuple Elements
tup = tuple("Geeks")
print(tup[0])  # Output: G
print(tup[-1])  # Output: s
print(tup[1:4])  # Output: ('e', 'e', 'k')

# Tuple Unpacking
tup = ("Geeks", "For", "Geeks")
a, b, c = tup
print(a)  # Output: Geeks
print(b)  # Output: For
print(c)  # Output: Geeks

# Concatenation of Tuples
tup1 = (0, 1, 2, 3)
tup2 = ('Geeks', 'For', 'Geeks')
tup3 = tup1 + tup2
print(tup3)  # Output: (0, 1, 2, 3, 'Geeks', 'For', 'Geeks')

# Slicing of Tuples
tup = tuple('GEEKSFORGEEKS')
print(tup[1:])  # Output: ('E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S')
print(tup[::-1])  # Output: ('S', 'K', 'E', 'E', 'G', 'R', 'O', 'F', 'S', 'K', 'E', 'E', 'G')
print(tup[4:9])  # Output: ('S', 'F', 'O', 'R', 'G')

# Deleting a Tuple
tup = (0, 1, 2, 3, 4)
del tup
# print(tup)  # This will raise an error (NameError)

# Tuple Unpacking with Asterisk (*)
tup = (1, 2, 3, 4, 5)
a, *b, c = tup
print(a)  # Output: 1
print(b)  # Output: [2, 3, 4]
print(c)  # Output: 5
