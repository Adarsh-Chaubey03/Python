def sumAll(*args):
   print(*args)
   return sum(args)

print(sumAll(1,23,4))
print(sumAll(1,23,4,23))
print(sumAll(1,23,4,2323,323))