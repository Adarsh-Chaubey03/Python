# Given a List of Number -- Count Positive Numbers 
num = [1,2,3,4,-2,-2,1,3,4,-3,3]
positive_number_count = 0
for x in num:
    if x > 0:
        positive_number_count += 1
print("Final Count: ", positive_number_count)
