# Parent class
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"

# Child class 1
class ElectricCar(Vehicle):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity

    def display_info(self):
        return f"{super().display_info()} - Battery: {self.battery_capacity} kWh"

# Child class 2
class Truck(Vehicle):
    def __init__(self, brand, model, year, payload_capacity):
        super().__init__(brand, model, year)
        self.payload_capacity = payload_capacity

    def display_info(self):
        return f"{super().display_info()} - Payload: {self.payload_capacity} tons"

# Creating objects
ev = ElectricCar("Tesla", "Model S", 2023, 100)
truck = Truck("Ford", "F-150", 2023, 5)

#print(ev.display_info())
#print(truck.display_info())

# vehicles = [ElectricCar("Tesla", "Model S", 2023, 100),Truck("Ford", "F-150", 2023, 5)]
vehicles = [ev,truck]

for vh in vehicles:
    print(vh.display_info())