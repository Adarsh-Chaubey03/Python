# basic.py

# String in Python
# A string is a sequence of characters enclosed in quotes.
# Python does not have a separate character type; a single character is just a string of length one.

# Creating Strings
s1 = 'GfG'  # Using single quotes
s2 = "GfG"  # Using double quotes

print(s1)  # Output: GfG
print(s2)  # Output: GfG

# Multi-line Strings
multi_line_1 = """I am Learning 
Python String on GeeksforGeeks"""
print(multi_line_1)
# Output:
# I am Learning
# Python String on GeeksforGeeks

multi_line_2 = '''I'm a  
Geek'''
print(multi_line_2)
# Output:
# I'm a  
# Geek

# Accessing Characters in Strings
s = "GeeksforGeeks"
print(s[0])   # Output: G (first character)
print(s[4])   # Output: s (fifth character)

print(s[-10])  # Output: k (third character from the start)
print(s[-5])   # Output: G (fifth character from the end)

# String Slicing
print(s[1:4])    # Output: eek (characters from index 1 to 3)
print(s[:3])     # Output: Gee (from start to index 2)
print(s[3:])     # Output: ksforGeeks (from index 3 to end)
print(s[::-1])   # Output: skeeGrofskeeG (reversed string)

# String Iteration
s = "Python"
for char in s:
    print(char)
# Output:
# P
# y
# t
# h
# o
# n

# String Immutability
s = "geeksforGeeks"
s = "G" + s[1:]  # Create a new string with the first character updated
print(s)  # Output: GeeksforGeeks

# Deleting a String
s = "GfG"
del s
# After deletion, accessing s will raise a NameError

# Updating a String
s = "hello geeks"
s1 = "H" + s[1:]  # Update first character
s2 = s.replace("geeks", "GeeksforGeeks")  # Replace word
print(s1)  # Output: Hello geeks
print(s2)  # Output: hello GeeksforGeeks

# Common String Methods
s = "GeeksforGeeks"
print(len(s))  # Output: 13 (length of the string)

s = "Hello World"
print(s.upper())  # Output: HELLO WORLD
print(s.lower())  # Output: hello world

s = "   Gfg   "
print(s.strip())  # Output: Gfg

s = "Python is fun"
print(s.replace("fun", "awesome"))  # Output: Python is awesome

# Concatenating and Repeating Strings
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)  # Output: Hello World

s = "Hello "
print(s * 3)  # Output: Hello Hello Hello

# Formatting Strings
name = "Alice"
age = 22
print(f"Name: {name}, Age: {age}")  # Output: Name: Alice, Age: 22

s = "My name is {} and I am {} years old.".format("Alice", 22)
print(s)  # Output: My name is Alice and I am 22 years old.

# String Membership Testing
s = "GeeksforGeeks"
print("Geeks" in s)  # Output: True
print("GfG" in s)  # Output: False

