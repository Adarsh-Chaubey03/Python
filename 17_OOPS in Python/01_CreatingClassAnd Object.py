## Creating Class And Object

# class Car:
#     brand = None
#     model = None

class Car:
    def __init__(self,brand,model): # Constructor
        self.brand = brand
        self.model = model

# Creating an object of the class Car
# Car()
myCar = Car("Toyota","Corola") 
print(myCar)
print(myCar.brand)  # Toyota

myCar2 = Car("Tata", "Safari")
print(myCar2.model) # Safari


# def __init__(self,ubrand,uModel):
# TypeError: Car.__init__() takes 2 positional arguments but 3 were given
# Every method inside a class automatically receives the object instance itself as its very first argument.
# While you only passed two arguments ("Toyota", "Corola"), Python automatically passed a third one for you: the myCar object that is being created.
# By convention, this first argument is always named self.
# Similar to 'this' in other language

# The Problem
# Your __init__ method is defined to accept two arguments:
# def __init__(ubrand, uModel):
# But when you call myCar = Car("Toyota", "Corola"), Python actually tries to run it like this:
# __init__(myCar, "Toyota", "Corola")
