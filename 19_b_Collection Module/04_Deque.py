# deque in Python
# deque (Double-Ended Queue) allows fast insertion and deletion from both ends

from collections import deque

# Basic deque creation
de = deque(['name', 'age', 'DOB'])
print(de)
# Output: deque(['name', 'age', 'DOB'])

# Appending and deleting elements
dq = deque([10, 20, 30])

dq.append(40)        # add to right
dq.appendleft(5)     # add to left
dq.extend([50, 60, 70])
print(dq)
# Output: deque([5, 10, 20, 30, 40, 50, 60, 70])

dq.extendleft([0, 5])
print(dq)
# Output: deque([5, 0, 5, 10, 20, 30, 40, 50, 60, 70])

dq.remove(20)
print(dq)
# Output: deque([5, 0, 5, 10, 30, 40, 50, 60, 70])

dq.pop()       # remove from right
dq.popleft()   # remove from left
print(dq)
# Output: deque([0, 5, 10, 30, 40, 50, 60])

dq.clear()
print(dq)
# Output: deque([])

# Accessing elements and length
dq = deque([1, 2, 3, 3, 4, 2, 4])
print(dq[0])
# Output: 1

print(dq[-1])
# Output: 4

print(len(dq))
# Output: 7

# Count, rotate, reverse
dq = deque([10, 20, 30, 40, 50, 20, 30, 20])

print(dq.count(20))
# Output: 3

print(dq.count(30))
# Output: 2

dq.rotate(2)
print(dq)
# Output: deque([30, 20, 10, 20, 30, 40, 50, 20])

dq.rotate(-3)
print(dq)
# Output: deque([20, 30, 40, 50, 20, 30, 20, 10])

dq.reverse()
print(dq)
# Output: deque([10, 20, 30, 20, 50, 40, 30, 20])
