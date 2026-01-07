#User function Template for python3
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

# 1. Use zip() to combine multiple lists into a single iterable 
zipped = zip(list1,list2)
print(list(zipped))  # Converts to list for display

# 2. Use filter() with lambda function to filter out numbers less than 3 in list1 

filtered = filter(lambda x : x<3,list1)
print(list(filtered))

# 3. Using map() with lambda function to multiply each number of list1 by 2
mapped = map(lambda x: x*2,list1)
print(list(mapped))
