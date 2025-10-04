# Add a static method to Car class that returns a general description of the car

# static method- method that belongs to class rather than instance of the class. Object Cannot
# access it.

class Car:  
    def __init__(self,brand,model): 
        self.__brand = brand 
        self.model = model
    
    def get_brand(self):
        return self.brand + "!"
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    @staticmethod
    def general_description(): # No need of self as object can't ever access it
        return "Cars are means of transport"


class ElectricCar(Car):
    def __init__(self, brand, model,batttery_size):
        self.battery_size = batttery_size
        super().__init__(brand, model)      
    
        
    def fuel_type(self):
        return "Electric Charge"

test = Car("Tata","Diesel")
# print(test.general_description()) # can't access the static method

print(Car.general_description()) # Cars are means of transport
