class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age}, City: {self.city})"

# Creating an object
person1 = Person("Alice", 25, "New York")
print(person1)   #person1.__str__()




