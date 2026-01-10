# The Counter is a subclass of Python’s dict from the collections module. 
# It is mainly used to count the frequency of elements in an iterable (like lists, strings or tuples) or from a mapping (dictionary).

from collections import Counter

# Create Counter from list
nums = [1, 2, 2, 3, 3, 3]
cnt = Counter(nums)
print(cnt)

# Create Counter from dict and string
ctr1 = Counter({1: 2, 2: 3})
ctr2 = Counter("hello")
print(ctr1)
print(ctr2)

# Access elements
print(cnt[2])   # existing key
print(cnt[5])   # non-existing key -> 0

# Update counts
cnt.update([2, 3, 3])
print(cnt)

# Most common elements
print(cnt.most_common(2))

# Elements expanded
print(list(cnt.elements()))

# Subtract counts
cnt.subtract([2, 3])
print(cnt)

# Arithmetic operations
a = Counter([1, 2, 2, 3])
b = Counter([2, 3, 3, 4])

print(a + b)   # addition
print(a - b)   # subtraction
print(a & b)   # intersection
print(a | b)   # union
