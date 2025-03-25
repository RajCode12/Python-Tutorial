# Vehicle class
class Vehicle:

    # Vehicle class constructor
    def __init__(self,make,model,year,price,fuel_type):
        self.make = make 
        self.model = model 
        self.year = year 
        self.price = price 
        self.fuel_type = fuel_type 
    
    # default print function
    def __str__(self):
        return f"{self.make} {self.model} {self.year} {self.price} {self.fuel_type}"

# EVCar class  
class EVCar(Vehicle):

    # EVCar class constructor
    def __init__(self,make,model,year,price,battery_capacity):
        super().__init__(make,model,year,price,battery_capacity)
        self.battery_capacity = battery_capacity
    
    # default print function
    def __str__(self):
        return f"{super().__str__()} {self.battery_capacity}"

# DieselCar class
class DieselCar(Vehicle):

    # Diesel car constructor
    def __init__(self,make,model,year,price,engine_capacity):
        super().__init__(make,model,year,price,engine_capacity)
        self.engine_capacity = engine_capacity

    # default print function 
    def __str__(self):
        return f"{super().__str__()} {self.engine_capacity}"

# Vehicle Inventory class 
class VehicleInventory:

    # default constructor
    def __init__(self):
        self.vehicles = []

    # function to add vehicle to the inventory
    def add_vehicle(self,vehicle):
        self.vehicles.append(vehicle)
        
    # function to remove vehicle from the inventory
    def remove_vehicle(self,vehicle):
        pass 

    # function to search vehicle by make in the inventory
    def search_by_make(self,vehicle_make):
        lst = []
        for vehicle in self.vehicles:
            if vehicle.make == vehicle_make:
                lst.append(vehicle)
        return lst

    # function to search vehicle by model in the inventory
    def search_by_model(self,vehicle_model):
        lst = []
        for vehicle in self.vehicles:
            if vehicle.model == vehicle_model:
                lst.append(vehicle)
        return lst

    # function to search vehicle by year in the inventory
    def search_by_year(self,vehicle_year):
        lst = []
        for vehicle in self.vehicles:
            if vehicle.year == vehicle_year:
                lst.append(vehicle)
        return lst

    # function to select every vehicle that falls in a range(min,max)
    def search_by_price_range(self,min,max):
        lst = []
        for vehicle in self.vehicles:
            if vehicle.price in range(min,max+1):
                lst.append(vehicle)
        return lst 
    
    # function to display all vehicles 
    def display_vehicles(self):
        for vehicle in self.vehicles:
            print(vehicle)
    
    # function to check if every vehicle has same year
    def check_same_year(self):
        price = 0
        for i in range(0,len(self.vehicles)):
            if i == 0:
                price = self.vehicles[i].price
            else:
                if price != self.vehicles[i].price:
                    return False    
        return True
                
# Test cases 

evCar1 = EVCar('Tesla','Model S',2022,100000,100.0)
evCar2 = EVCar('BMW','i4',2022,100000,100.0)
dieselCar1 = DieselCar('Toyota','Corolla',2020,20000,1.8)
dieselCar2 = DieselCar('Tata','Nexon',2020,20000,1.8)
print('*************************************************')

inventory = VehicleInventory()
inventory.add_vehicle(evCar1)
inventory.add_vehicle(evCar2)
inventory.add_vehicle(dieselCar1)
inventory.add_vehicle(dieselCar2)
print('*************************************************')

inventory.display_vehicles()
print('*************************************************')

vehicle_list_by_make = inventory.search_by_make('Tesla')
for vehicle in vehicle_list_by_make:
    print(vehicle)
print('*************************************************')

vehicle_list_by_model = inventory.search_by_model('Model S')
for vehicle in vehicle_list_by_model:
    print(vehicle)
print('*************************************************')

vehicle_list_by_year = inventory.search_by_year(2020)
for vehicle in vehicle_list_by_year:
    print(vehicle)
print('*************************************************')

vehicle_list_by_price_range = inventory.search_by_price_range(50000,150000)
for vehicle in vehicle_list_by_price_range:
    print(vehicle)
print('*************************************************')

same_year = inventory.check_same_year()
print(same_year)
 
    
    
