# Create two classes Battery and Engine and let an ElectricCar class inherit from both

class Car:  
    def __init__(self,brand,model): 
        self.__brand = brand 
        self.model = model
    
    def get_brand(self):
        return self.brand + "!"
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self, brand, model,batttery_size):
        self.battery_size = batttery_size
        super().__init__(brand, model)    






class Battery:
    def battery_info(self):
        return "This is battery."

class Engine:
    def Engine_info(self):
        return "This is Engine."

  

class ElectricCar2(Battery,Engine,Car):
    pass



myTesla = ElectricCar2("Tesla","Model S")

print(myTesla.Engine_info()) # This is Engine.
print(myTesla.battery_info()) # This is battery.

