'''
In Python, every value has an inherent Boolean evaluation, it can either be considered True or False in a Boolean context. 

Truthy Values

These evaluate to True in a Boolean context:
Non-empty sequences or collections: [ 1 ], ( 0, ), "Hello", { 1:2 }
Numeric values not equal to zero: 1, -4, 3.5
Constant: True

Falsy Values
These evaluate to False in a Boolean context:

Empty sequences and collections: [ ], ( ), { }, set( ), " ", range(0)
Numbers: 0 (integer), 0.0 (float), 0j (complex)
Constants: None, False

'''

number = 7
if number:
    print("This will be printed as 7 is truthy value")

number = 0
if number:
    print("This will be not printed as 0 is falsy value")
    
# One can check if a value is either truthy or falsy with built-in bool() function.
print(bool(7))     # True 
print(bool(0))      # False
print(bool([1,2,3])) # True 
print(bool([]))   # False   
print(bool(None)) # False