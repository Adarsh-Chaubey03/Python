# Python filter() function
# filter(function, iterable)
# It filters elements from an iterable for which the function returns True
# and returns a filter object (iterator).

# 1. Filter even numbers using a normal function
def even(x):
    return x % 2 == 0

a = [1, 2, 3, 4, 5, 6]
b = filter(even, a)
print(list(b))   # [2, 4, 6]

# 2. Filter even numbers using lambda
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)
print(list(b))   # [2, 4, 6]

# 3. Filter even numbers and then double them
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)
c = map(lambda x: x * 2, b)
print(list(c))   # [4, 8, 12]

# 4. Filter strings with length greater than 5
a = ["apple", "banana", "cherry", "kiwi", "grape"]
b = filter(lambda w: len(w) > 5, a)
print(list(b))   # ['banana', 'cherry']

# 5. Filter falsy values using None
L = ["apple", "", None, "banana", 0, "cherry"]
A = filter(None, L)
print(list(A))   # ['apple', 'banana', 'cherry']
