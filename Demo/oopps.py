from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self,name,price,mileage):
        self.name = name 
        self.price = price 
        self.mileage = mileage 

    def __str__(self):
        return f"{self.name} {self.price} {self.mileage}"
    
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass 

class Truck(Vehicle):
    def __init__(self,name,price,mileage,payload):
        super().__init__(name,price,mileage)
        self.payload = payload 
    
    def __str__(self):
        return f"{super().__str__()} {self.payload}"
    
    def start_engine(self):
        print("truck engine started...")

    def stop_engine(self):
        print("truck engine stopped...")

class Bike(Vehicle):
    def __init__(self,name,price,mileage,top_speed):
        super().__init__(name,price,mileage)
        self.top_speed = top_speed
    
    def __str__(self):
        return f"{super().__str__()} {self.top_speed}"
    
    def start_engine(self):
        print("bike engine started...")

    def stop_engine(self):
        print("bike engine stopped...")

class Inventory():
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self,vehicle):
        self.vehicles.append(vehicle)

    def search_vehicle(self,vehicle_name):
        for v in self.vehicles:
            if v.name == vehicle_name:
                return v
        return None 

    def update_vehicle(self,vehicle_name,mileage=None,payload=None,top_speed=None):
        vehicle = self.search_vehicle(vehicle_name)
        if vehicle:
            if mileage:
                vehicle.mileage = mileage
            if payload:
                vehicle.payload = payload 
            if top_speed:
                vehicle.top_speed = top_speed 
        
    def delete_vehicle(self,vehicle_name):
        vehicle = self.search_vehicle(vehicle_name)
        self.vehicles.remove(vehicle)
        
    def display_vehicles(self):
        for v in self.vehicles:
            print(v)

bike1 = Bike('Bike1',100000,40,140)
bike2 = Bike('Bike2',120000,35,150)

truck1 = Truck('Truck1',500000,50,1000)
truck2 = Truck('Truck2',600000,40,1200)

inventory = Inventory()
inventory.add_vehicle(bike1)
inventory.add_vehicle(bike2)
inventory.add_vehicle(truck1)
inventory.add_vehicle(truck2)
inventory.display_vehicles()

print("***********************************************")

vehicle1 = inventory.search_vehicle('Truck1')
if vehicle1:
    print(vehicle1, " found...")

print("***********************************************")

inventory.update_vehicle('Bike2',mileage = 45,top_speed = 160)
inventory.update_vehicle('Truck2',mileage = 45,payload = 1500)
inventory.display_vehicles()

print("***********************************************")

inventory.delete_vehicle('Truck2')
inventory.delete_vehicle('Bike2')
inventory.display_vehicles()

