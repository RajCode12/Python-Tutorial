#1. CSV**

import csv

# Employee class

class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __str__(self):
        return f"{self.name} {self.age} {self.salary}"

# Creating list of employee objects

emp1 = Employee("Raj",22,10000)
emp2 = Employee("Dev",21,20000)
emp3 = Employee("Gourav",23,20000)
employees = [emp1,emp2,emp3]

#**1. CSV (.csv)**

with open('employees.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'age', 'salary']  # assuming these are the attributes of Employee class
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for employee in employees:
        writer.writerow({k: getattr(employee, k) for k in fieldnames})

# reading from CSV file
with open('employees.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)  # prints a dictionary representing an Employee object


#**2. Excel (.xlsx)**

import xlsxwriter

workbook = xlsxwriter.Workbook('employees.xlsx')
worksheet = workbook.add_worksheet()

fieldnames = ['name', 'age', 'salary']  # assuming these are the attributes of Employee class

for i, employee in enumerate(employees):
    for j, field in enumerate(fieldnames):
        worksheet.write(i, j, getattr(employee, field))

workbook.close()


#**3. Text (.txt)**

with open('employees.txt', 'w') as f:
    for employee in employees:
        f.write(str(employee))  # assuming __str__ method is defined in Employee class to return a string representation of the object

# reading from text file
with open('employees.txt', 'r') as f:
    for line in f:
        print(line)  # prints a string representation of an Employee object

#**4. JSON**

import json

data = [{'name': employee.name, 'age': employee.age, 'salary': employee.salary} for employee in employees]

with open('employees.json', 'w') as f:
    json.dump(data, f)

# reading from JSON file
with open('employees.json', 'r') as f:
    data = json.load(f)
    for employee_data in data:
        print(employee_data)  # prints a dictionary representing an Employee object
