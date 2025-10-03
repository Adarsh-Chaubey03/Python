
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


class ElectricCar(Car):
    def __init__(self, brand, model,batttery_size):
        self.battery_size = batttery_size
        super().__init__(brand, model)      
    
        
    def fuel_type(self):
        return "Electric Charge"




myTesla = ElectricCar("Tesla","Model S","85KwH")
safari = Car("Tata","Diesel")

print(myTesla.fuel_type())  # Electric Charge
print(safari.fuel_type())   # Petrol or Diesel
