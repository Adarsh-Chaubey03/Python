import math

def juggler_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = int(math.sqrt(n))
        else:
            n = int(n ** 1.5)
        sequence.append(n)
    return sequence


print(juggler_sequence(3))
