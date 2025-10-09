#  print a table upto 10 skip fifth StopIterati
n = 3
for i in range(1, 11):
    if i == 5:      # skip the 5th multiple
        continue
    print(n, 'x', i, '=', n * i)
