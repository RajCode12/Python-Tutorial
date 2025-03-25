#Factory Management System (Multiple Inheritance)
class PetrolCar:
    def start(self):
        return "car starts with petrol"

class CNGCar:
    def start(self):
        return "car starts with CNG"

class HybridCar(PetrolCar,CNGCar):#Multiple Inheritance
    def start(self):
        return "car starts with Petrol or CNG"

# Creating object
my_car = HybridCar()
print(my_car.start())
