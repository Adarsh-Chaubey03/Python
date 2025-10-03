# Make brand attribute private and create a getter method to access brand attribute using this method
# This will prevent direct access 


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


myTesla = ElectricCar("Tesla","Model S","85KwH")

print(myTesla.__brand)        # Tesla
print(myTesla.get_brand())  # Tesla!