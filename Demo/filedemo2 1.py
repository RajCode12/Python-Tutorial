import json

'''
JSON (JavaScript Object Notation) is a popular data format 
used for representing structured data. It's common to transmit
 and receive data between a server and web application in JSON format.
JSON stands for JavaScript Object Notation and
is a lightweight format for storing and transporting data.
JSON is often used when data is sent from a server to a web page.
Python has the built-in module json , which allow us to work with JSON data.
'''
# Data to write
data = {
    'people': [
        {'Name': 'Ajay', 'Age': 30, 'City': 'Pune'},
        {'Name': 'Harish', 'Age': 25, 'City': 'Delhi'},
        {'Name': 'Eshan', 'Age': 35, 'City': 'Mumbai'}
    ]
}

# Writing to a JSON file
with open('people.json', 'w') as file:
    json.dump(data, file,indent=4)

print("Data written to people.json")

# Reading from a JSON file
with open('people.json', 'r') as file:
    data = json.load(file)
    print(data)
