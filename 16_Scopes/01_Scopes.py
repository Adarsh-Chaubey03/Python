username = "chaiaurcode"

def func():
    username = "chai"
    # If this username is removed func will print the username in global scope
    # Accessing variables flow from smaller to larger scope
    print(username)

print(username) # chaiaurcode
func() # chai

x = 99

# def func2(y):
#     z=x+y
#     return z

# result = func2(1)
# print(result)  # 100


def func3():
    x = 88 # new x is created
    print(x)

print(x)  # 99
func3()   # 88 
print(x)  # 99

def func4():
    global x  # global x is accessed
              # bad coding --> access global variables but do not change unless very important
              #-- avoid it -- other developers might get affeced
    x = 12    

func4()
print(x)  # 12


def f1():
    x = 88
    def f2():
        print(x)
    return f2
myResult = f1()
myResult() # 88


# closures
def chai(num):
    def actual(x):
        return x ** num
    return actual

f = chai(2)
g = chai(3)

print(f) # <function chai.<locals>.actual at 0x000002943177C4A0>
print(f(3)) # 9
print(g(3)) # 27
