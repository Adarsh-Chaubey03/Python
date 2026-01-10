# OrderedDict in Python
# OrderedDict is a dictionary subclass that remembers insertion order
# It is used when key order must be preserved and manipulated

from collections import OrderedDict

# Basic creation
od = OrderedDict()
od['apple'] = 1
od['banana'] = 2
od['cherry'] = 3
print(od)
# Output: OrderedDict([('apple', 1), ('banana', 2), ('cherry', 3)])

# Order is preserved
for k, v in od.items():
    print(k, v)
# Output:
# apple 1
# banana 2
# cherry 3

# Changing value does NOT change order
od['banana'] = 5
print(od)
# Output: OrderedDict([('apple', 1), ('banana', 5), ('cherry', 3)])

# Equality check considers order
od1 = OrderedDict([('a', 1), ('b', 2)])
od2 = OrderedDict([('b', 2), ('a', 1)])
print(od1 == od2)
# Output: False

# Pop items from end and front
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od.popitem(last=True))
# Output: ('c', 3)

print(od.popitem(last=False))
# Output: ('a', 1)

# Move keys
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od.move_to_end('a')
od.move_to_end('b', last=False)
print(od)
# Output: OrderedDict([('b', 2), ('c', 3), ('a', 1)])

# Delete and reinsert moves key to end
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od.pop('c')
print(od)
# Output: OrderedDict([('a', 1), ('b', 2)])

od['c'] = 3
print(od)
# Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
