# Taking input without prompt
print("Enter a name")
name = input()
print("Name entered is", name)

# Taking input with prompt inside input()
name = input("Enter another name: ")
print("Another name entered is", name)

# Taking multiple inputs in a single line using split()
x, y = input("Enter two values: ").split()
print("Number of boys:", x)
print("Number of girls:", y)

# ❌ Incorrect way to take multiple inputs
# x, y = input("Enter two values:")
# Reason:
# input() returns a single string.
# Without split(), Python cannot unpack multiple values.
# This causes:
# ValueError: too many values to unpack (expected 2)

# ✅ Correct way to take multiple inputs
# split() breaks the input string into multiple values
