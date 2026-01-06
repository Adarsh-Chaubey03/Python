# Python map() 
# map(function, iterable)

# 1. Convert string numbers to integers
nums_str = ['1', '2', '3', '4']
nums_int = list(map(int, nums_str))
print(nums_int)   # [1, 2, 3, 4]

# 2. Double each number using a normal function
def double(x):
    return x * 2

nums = [1, 2, 3, 4]
doubled = list(map(double, nums))
print(doubled)    # [2, 4, 6, 8]

# 3. Square numbers using lambda
squared = list(map(lambda x: x * x, nums))
print(squared)    # [1, 4, 9, 16]

# 4. Add elements of two lists
a = [1, 2, 3]
b = [4, 5, 6]
summed = list(map(lambda x, y: x + y, a, b))
print(summed)     # [5, 7, 9]

# 5. Convert strings to uppercase
words = ['apple', 'banana', 'cherry']
upper_words = list(map(str.upper, words))
print(upper_words)  # ['APPLE', 'BANANA', 'CHERRY']
