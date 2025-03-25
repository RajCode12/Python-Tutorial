class Car:
    #constructor function
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def __str__(self):
        return f"({self.brand} {self.model} {self.year})"
   
    
# Creating an object
car1 = Car("Toyota", "Corolla", 2022)
print(car1)     # print(car1.__str__())
car2 = Car("Sedan", "Audi", 2020)
print(car2)  # print(car2.__str__())
print(car1.model) 



