class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def display_info(self):
        return f"Vehicle: {self.brand} {self.model}"
    

class Car(Vehicle):
    def __init__(self,brand,model,fuel_type):
        super().__init__(brand,model)
        self.fuel_type=fuel_type
    
    def display_info(self):
        return f"Car: {self.brand} {self.model}, Fuel: {self.fuel_type}"
    

class ElectricCar(Car):
    def __init__(self,brand,model,battery_capacity):
        super().__init__(brand,model,"Electric")
        self.battery_capacity = battery_capacity
        
    def display_info(self):
        return f"Electric Car: {self.brand} {self.model}, Battery: {self.battery_capacity}"
    
    
vehicle = Vehicle("Generic", "ModelX")
car = Car("Toyota","Corolla","Petrol")
electric_car = ElectricCar("Tesla","Model S",100)

print(vehicle.display_info())
print(car.display_info())
print(electric_car.display_info())