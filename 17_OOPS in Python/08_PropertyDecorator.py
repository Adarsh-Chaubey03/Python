# make model attribute read only

class Car:  
    def __init__(self,brand,model): 
        self.__brand = brand 
        self.__model = model
    
    def get_brand(self):
        return self.brand + "!"
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    @staticmethod
    def general_description(): # No need of self as object can't ever access it
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model,batttery_size):
        self.battery_size = batttery_size
        super().__init__(brand, model)      
    
        
    def fuel_type(self):
        return "Electric Charge"

test = Car("Tata","Diesel")
# test.model = "City" # Property model has no setter method

print(test.model) # Diesel