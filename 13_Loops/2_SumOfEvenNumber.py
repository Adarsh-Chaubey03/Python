# Sum of Even Number upto N
N = 20
sum_even = 0

for x in range(1,N+1):
    if x % 2 == 0:
        sum_even += x

print("Sum of even number: ",sum_even)