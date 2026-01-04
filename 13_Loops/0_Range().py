# Syntax of range() Method
# range(start, stop, step)

# Parameters:
# start(optional): The starting value of the sequence. Default is 0.
# stop(required): The ending value of the sequence (exclusive).
# step(optional): The difference between each number in the sequence. Default is 1.

def stringJumper(s):
    # Jump by 2 to access only even indices
    for i in range(0, len(s), 2):
        print(s[i], end="")
    print()


# Input 1
s = "DoctorPhenomenal"
stringJumper(s)
# Output: DcoPeoea

# Input 2
s = "Geeks"
stringJumper(s)
# Output: Ges
