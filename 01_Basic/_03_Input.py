# Taking input without a prompt
print("Enter a name")
name = input()
print("Name entered is", name)

# Taking input with a prompt inside input()
name = input("Enter another name: ")
print("Another name entered is", name)

# Taking multiple inputs in a single line using split()
x, y = input("Enter two values: ").split()  # split() breaks input into multiple values
print("Number of boys:", x)
print("Number of girls:", y)

# Note: Using split() is necessary to unpack multiple inputs. Without it, you'd get a ValueError.
# as input() accepts value as single string
