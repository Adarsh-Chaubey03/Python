# In Python, variable types are inferred from the assigned value, no explicit type declaration is needed.

# Valid variables
age = 1
name = "adarsh"
print(age)
print(name)

# Invalid variables (examples, not executed)
# 1name = "Error"  # Starts with a digit
# class = 10       # 'class' is a reserved keyword
# user-name = "Doe"  # Contains a hyphen

# Example of type flexibility
x = 10
x = "Now a string"
print(x)  # Outputs: Now a string

# Basic type casting
s = "10"
n = int(s)
print(n)
