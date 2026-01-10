# defaultdict in Python
# defaultdict is a dict subclass that provides a default value for missing keys
# It avoids KeyError by automatically creating missing keys

from collections import defaultdict

# Example 1: list as default factory
d = defaultdict(list)
d['fruits'].append('apple')
d['vegetables'].append('carrot')
print(d)
# Output: defaultdict(<class 'list'>, {'fruits': ['apple'], 'vegetables': ['carrot']})

print(d['juices'])
# Output: []

# Example 2: list default factory with loop
d = defaultdict(list)
for i in range(5):
    d[i].append(i)
print(d)
# Output: defaultdict(<class 'list'>, {0: [0], 1: [1], 2: [2], 3: [3], 4: [4]})

# Example 3: int as default factory (counting)
d = defaultdict(int)
arr = [1, 2, 3, 4, 2, 4, 1, 2]
for x in arr:
    d[x] += 1
print(d)
# Output: defaultdict(<class 'int'>, {1: 2, 2: 3, 3: 1, 4: 2})

# Example 4: str as default factory
sd = defaultdict(str)
sd['greeting'] = 'Hello'
print(sd)
# Output: defaultdict(<class 'str'>, {'greeting': 'Hello'})

# Example 5: grouping words by first letter
words = ["apple", "ant", "banana", "bat", "carrot", "cat"]
grouped = defaultdict(list)
for word in words:
    grouped[word[0]].append(word)
print(grouped)
# Output: defaultdict(<class 'list'>,
# {'a': ['apple', 'ant'], 'b': ['banana', 'bat'], 'c': ['carrot', 'cat']})

# Example 6: custom default factory
d = defaultdict(lambda: "Not Present")
d["a"] = 1
d["b"] = 2

print(d["x"])
# Output: Not Present

print(d["a"])
# Output: 1
