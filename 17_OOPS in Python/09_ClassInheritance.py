# Demonstrate the use of isinstance() to check if myTestla is an instance of Car and ElectricCar


class Car:  
    def __init__(self,brand,model): 
        self.__brand = brand # __ => before any attribute makes it private
        self.model = model
    
    def get_brand(self):
        return self.brand + "!"
    
    def full_name(self):
        return f"{self.__brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model,batttery_size):
        self.battery_size = batttery_size
        super().__init__(brand, model)      


myTesla = ElectricCar("Tesla","Model S","85KwH")

print(isinstance(myTesla,Car))   # True
print(isinstance(myTesla,ElectricCar))  #True