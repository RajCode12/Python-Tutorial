import pandas as pd 

# loading csv file data into dataframe
df1 = pd.read_csv('sales_data_2022.csv')
print(df1)
print('*******************************************')

df2 = pd.read_csv('sales_data_2023.csv')
print(df2)
print('*******************************************')

# merging two data frame 
merge_df = pd.merge(df1,df2,'outer')
print(type(merge_df))

print('*******************************************')

# data with columns 
data = [['North','ProductA',1000],['North','ProductA',1200],['North','ProductB',2000],
        ['North','ProductB',2200],['South','ProductA',1500],['South','ProductA',1800],
        ['South','ProductB',2500],['South','ProductB',2800]]
df3 = pd.DataFrame(data,columns=['Region','Product','Sales'])
#print(df3)
print('*******************************************')

total_sales_by_region = merge_df.groupby('Region')['Sales'].sum()
# total sales for each region 
total_sales_by_region = df3.groupby('Region')['Sales'].sum()
print('Total Sales by Region : ')
print(total_sales_by_region)
print('*******************************************')

# total sales for each product
total_sales_by_product = df3.groupby('Product')['Sales'].sum().reset_index()
print('Total Sales by Product : ')
print(total_sales_by_product)
print('*******************************************')

# region with highest total sales
highest_sales_region = df3.groupby('Region')['Sales'].sum().idxmax()
print('Top Region : ', highest_sales_region)
print('*******************************************')

# product with highest total sales
highest_sales_product = df3.groupby('Product')['Sales'].sum().idxmax()
print('Top Product : ', highest_sales_product)