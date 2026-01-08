# Python Arrays - Core Concepts

import array as arr

# 1. Creating an array with a specific data type
array1 = arr.array('i', [1, 2, 3, 4])
print("Array of integers:", array1)

# 2. Accessing elements in an array by index
print("First element:", array1[0])
print("Fourth element:", array1[3])

# 3. Adding elements to an array using append()
array1.append(5)
print("Array after appending an element:", array1)

# 4. Inserting elements at a specific index
array1.insert(1, 6)
print("Array after inserting an element at index 1:", array1)

# 5. Removing elements from an array using remove()
array1.remove(6)
print("Array after removing an element:", array1)

# 6. Removing an element by index using pop()
popped_element = array1.pop(2)
print("Popped element:", popped_element)
print("Array after popping an element:", array1)

# 7. Slicing an array
array2 = arr.array('i', [10, 20, 30, 40, 50])
print("Sliced array (elements 1 to 3):", array2[1:4])

# 8. Searching for an element using index()
index_of_30 = array2.index(30)
print("Index of 30 in array:", index_of_30)

# 9. Updating elements in an array by index
array2[2] = 35
print("Array after updating an element at index 2:", array2)

# 10. Counting occurrences of an element
array3 = arr.array('i', [1, 2, 2, 3, 4, 2, 5])
count_of_2 = array3.count(2)
print("Count of 2 in array:", count_of_2)

# 11. Reversing the elements in an array
array3.reverse()
print("Reversed array:", array3)

# 12. Extending an array with another iterable
array3.extend([6, 7, 8])
print("Array after extending:", array3)
