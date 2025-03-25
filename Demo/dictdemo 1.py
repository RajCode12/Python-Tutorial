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
squared_numbers = {num: num**3 for num in numbers}
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
print(person["address"]["city"])
print(person["address"])

# Creating a list of dictionaries
people = [
    {"name": "John", "age": 30, "city": "Mumbai"},
    {"name": "Ajay", "age": 25, "city": "Pune"},
    {"name": "Anup", "age": 40, "city": "Delhi"}
]

print(people)

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = {**dict1, **dict2}
print(merged_dict) 

my_dict = {'name': 'John', 'age': 30}
print('name' in my_dict)  
print('city' in my_dict)  

keys = ['name', 'age', 'city']
values = ['John', 30, 'New York']

# Use zip() to pair corresponding elements from the two lists
pairs = list(zip(keys, values))
# Convert the list of pairs into a dictionary
my_dict = dict(pairs)
print(my_dict)


keys = ['name', 'age', 'city']
values = ['John', 30, 'New York']
# Use dictionary comprehension to create a dictionary
my_dict = {key: value for key, value in zip(keys, values)}
print(my_dict)

import itertools

my_list = [1, 2, 3]
result = list(itertools.permutations(my_list))
print(result)  # Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

import itertools

my_list = [1, 2, 3,4]
result = list(itertools.combinations(my_list, 2))
print(result)  


import itertools

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

result = list(itertools.chain(list1, list2))
print(result)  # Output: [1, 2, 3, 'a', 'b', 'c']

'''

itertools is a built-in Python module that provides a variety of tools intended to be fast and use memory efficiently when handling iterators (like lists, tuples, dictionaries, etc). The module provides functions that operate on iterables, allowing you to perform various operations such as loops, filtering, mapping, and more.

'''