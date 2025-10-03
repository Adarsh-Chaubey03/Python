class Car:
    def __init__(self,brand,model): # Constructor
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"
        

# Creating an object of the class Car
# Car()
myCar = Car("Toyota","Corola")
print(myCar.full_name) # <bound method Car.full_name of <__main__.Car object at 0x0000026421BB6A50>>
# full_name() is a method so we need to use paranthesis
print(myCar.full_name())  # Toyota Corola

myCar2 = Car("Tata", "Safari")

