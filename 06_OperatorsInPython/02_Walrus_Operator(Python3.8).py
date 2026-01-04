# walrus_operator.py

# Walrus Operator (:=) - Introduced in Python 3.8.
# Allows assigning a value and checking it in one line.

# Example: Using Walrus Operator in a While Loop
numbers = [1, 2, 3, 4, 5]

# Continue loop while the length of numbers is greater than zero.
while (n := len(numbers)) > 0:
    print(numbers.pop())

# Output:
# 5
# 4
# 3
# 2
# 1

# Explanation:
# This way, we assign and check the length in a single line, making the code cleaner.
