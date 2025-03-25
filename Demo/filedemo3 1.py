import xlsxwriter

# Data to write
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

# Create a new Excel file and add a worksheet
workbook = xlsxwriter.Workbook('people.xlsx')
worksheet = workbook.add_worksheet()

# Write data to the worksheet
for index, row_data in enumerate(data):
    #print(index,row_data)
    worksheet.write_row(index, 0, row_data)


workbook.close() # Close the workbook
print("Data written to people.xlsx")


import pandas as pd
# Reading from an Excel file
df = pd.read_excel('people.xlsx')
#print(type(df))
# Display the DataFrame
print(df)
