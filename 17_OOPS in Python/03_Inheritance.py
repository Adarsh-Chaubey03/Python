# Parent Class
class Car:  
    def __init__(self,brand,model): # Constructor
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"

# Child Class
class ElectricCar(Car):
    def __init__(self, brand, model,batttery_size):
        self.battery_size = batttery_size
        super().__init__(brand, model)        # super -> inherit all attribute of this method from parent class

myCar = Car("Toyota","Corola")
myTesla = ElectricCar("Tesla","Model S","85KwH")
print(myTesla.battery_size) # 85KwH
print(myTesla.model) # Model S
print(myTesla.full_name())