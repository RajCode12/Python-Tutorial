from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_id, make, model, year):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self, miles):
        self.mileage += miles

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    def display_details(self):
        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Mileage: {self.mileage} miles")

class Car(Vehicle):
    def __init__(self, vehicle_id, make, model, year, num_doors):
        super().__init__(vehicle_id, make, model, year)
        self.num_doors = num_doors

    def start_engine(self):
        print("Car engine started")

    def stop_engine(self):
        print("Car engine stopped")

class Truck(Vehicle):
    def __init__(self, vehicle_id, make, model, year, cargo_capacity):
        super().__init__(vehicle_id, make, model, year)
        self.cargo_capacity = cargo_capacity

    def start_engine(self):
        print("Truck engine started")

    def stop_engine(self):
        print("Truck engine stopped")

class Motorcycle(Vehicle):
    def __init__(self, vehicle_id, make, model, year, engine_size):
        super().__init__(vehicle_id, make, model, year)
        self.engine_size = engine_size

    def start_engine(self):
        print("Motorcycle engine started")

    def stop_engine(self):
        print("Motorcycle engine stopped")

class VehicleManager:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def search_vehicle(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                return vehicle
        return None

    def modify_vehicle(self, vehicle_id, make=None, model=None, year=None):
        vehicle = self.search_vehicle(vehicle_id)
        if vehicle:
            if make:
                vehicle.make = make
            if model:
                vehicle.model = model
            if year:
                vehicle.year = year

    def delete_vehicle(self, vehicle_id):
        vehicle = self.search_vehicle(vehicle_id)
        if vehicle:
            self.vehicles.remove(vehicle)

    def display_vehicles(self):
        for vehicle in self.vehicles:
            vehicle.display_details()
            print("------------------------")

# Create a list of Vehicle objects
manager = VehicleManager()
manager.add_vehicle(Car("CAR-001", "Toyota", "Camry", 2020, 4))
manager.add_vehicle(Truck("TRK-001", "Ford", "F-150", 2015, 2000))
manager.add_vehicle(Motorcycle("MOT-001", "Harley-Davidson", "Electra Glide", 2010, 107))
manager.add_vehicle(Car("CAR-002", "Honda", "Civic", 2018, 2))
manager.add_vehicle(Truck("TRK-002", "Chevrolet", "Silverado", 2012, 1500))
manager.add_vehicle(Motorcycle("MOT-002", "Yamaha", "FJR1300", 2015, 1298))

# Display all vehicles
print("All Vehicles:")
manager.display_vehicles()

# Search for a vehicle
print("Searching for vehicle CAR-001:")
vehicle = manager.search_vehicle("CAR-001")
if vehicle:
    vehicle.display_details()
else:
    print("Vehicle not found")

# Modify a vehicle
manager.modify_vehicle("CAR-001", make="Lexus")
print("Modified vehicle CAR-001:")
vehicle = manager.search_vehicle("CAR-001")
if vehicle:
    vehicle.display_details()
else:
    print("Vehicle not found")

# Delete a vehicle
manager.delete_vehicle("TRK-001")
print("All Vehicles after deletion:")
manager.display_vehicles()