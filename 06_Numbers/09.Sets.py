# Python Sets - Core Concepts

# 1. Creating a set using curly braces
set1 = {1, 2, 3, 4}
print("Set created with curly braces:", set1)

# 2. Creating a set using the set() function
set2 = set([5, 6, 7, 8])
print("Set created with set() function:", set2)

# 3. Sets are mutable and do not allow duplicates
set3 = {1, 2, 2, 3, 4}
print("Set with duplicates (duplicates removed):", set3)

# 4. Adding elements to a set
set3.add(5)
print("Set after adding an element:", set3)

# 5. Removing elements from a set
set3.discard(3)
print("Set after discarding an element:", set3)

# 6. Iterating over a set
print("Iterating over the set:")
for item in set3:
    print(item, end=' ')
print()

# 7. Checking membership in a set
print("Is 5 in the set?", 5 in set3)

# 8. Using frozenset (immutable set)
frozen = frozenset([10, 20, 30])
print("Frozenset:", frozen)

# 9. Typecasting a list to a set
list_example = [1, 2, 2, 3, 4, 5]
set_from_list = set(list_example)
print("Set from list:", set_from_list)
