# Python reduce() function
# reduce() applies a function cumulatively to elements of an iterable
# and reduces it to a single final value.
# Syntax: reduce(function, iterable[, initializer])

from functools import reduce
import operator

# 1. Concatenate strings
words = ["Geeks", "for", "Geeks"]
res = reduce(lambda x, y: x + " " + y, words)
print(res)   # Geeks for Geeks

# 2. Sum of numbers using named function
def add(x, y):
    return x + y

a = [1, 2, 3, 4, 5]
print(reduce(add, a))   # 15

# 3. Factorial using lambda
a = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x * y, a))   # 120

# 4. Using operator module
a = [1, 3, 5, 6, 2]
print(reduce(operator.add, a))   # 17
print(reduce(operator.mul, a))   # 180

# 5. Using initializer
a = [1, 2, 3]
print(reduce(lambda x, y: x + y, a, 10))   # 16
