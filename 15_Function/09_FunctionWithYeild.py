# Write a generator functon that yeilds even number upto specified limit 
def even_generator(limit):
     for i in range(2,limit+1,2):
          yield i
    # li=[]
    # for i in range(2,limit+1,2):
    #     li.append(i)
    # return li
    
for num in even_generator(10):
     print(num)