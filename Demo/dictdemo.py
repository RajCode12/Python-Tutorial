my_dict = {"name": "John", "age": 30, 1:200 }
print(my_dict["name"])  
print(my_dict["age"])   
print(my_dict[1])

my_dict = {"name": "John", "age": 30}
my_dict["age"] = 31
print(my_dict)

my_dict = {"name": "John", "age": 30}
my_dict["city"] = "New York"
print(my_dict) 

my_dict = {"name": "John", "age": 30, "city": "New York"}

# Using the del statement
del my_dict["city"]
print(my_dict)  

# Using the pop() method
print(my_dict.pop("age"))# remove spcified key and return corresponding value
print(my_dict)  

my_dict = {"name": "John", "age": 30}

print(my_dict.keys())  
print(my_dict.values())
print(my_dict.items()) 

print(my_dict.get("name"))  # if key not found it returns None
print(my_dict.get("NAME"))  # if key not found it returns None
print(my_dict.get("city", "Not found")) 

my_dict.update({"city": "New York"})
print(my_dict) 

# Iterating over keys
my_dict = {"name": "John", "age": 30, "city": "New York"}
for key in my_dict:
    print(key)

# Iterating over values
for value in my_dict.values():
    print(value)

# Iterating over items
for key, value in my_dict.items():
    print(f"{key}: {value}")
    
# Creating a new dictionary with squared values
numbers = [1, 2, 3, 4, 5]
squared_numbers = {num: num**2 for num in numbers}
print(squared_numbers)

# Creating a new dictionary with filtered items
my_dict = {"name": "John", "age": 30, "city": "New York"}
filtered_dict = {key: value for key, value in my_dict.items() if key != "age"}
print(filtered_dict)  

# Unpacking a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}
name, age, city = my_dict.values()
print(name)  
print(age)   
print(city)  

# Unpacking a dictionary with keyword arguments
def greet(name, age, city):
    print(f"Hello, my name is {name} and I am {age} years old from {city}.")

my_dict = {"name": "John", "age": 30, "city": "New York"}
greet(**my_dict) 

# Creating a nested dictionary
person = {
    "name": "John",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY",
        "zip": "10001"
    }
}

# Accessing values in a nested dictionary
print(person["name"])  
print(person["address"]["street"])  

# Creating a list of dictionaries
people = [
    {"name": "John", "age": 30, "city": "Mumbai"},
    {"name": "Ajay", "age": 25, "city": "Pune"},
    {"name": "Anup", "age": 40, "city": "Delhi"}
]

print(people)