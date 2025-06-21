"""Group the data by the Category column and calculate the following aggregate statistics for each category:
Total quantity sold.
Average price per unit.
Maximum quantity sold in a single transaction.
"""

import pandas as pd

# Group the data by the Category column and calculate the following aggregate statistics for each category:

sales = pd.read_csv(r'C:\Python\lesson-19\homework\sales_data.csv', index_col='Product')


grouped_by_category = sales.groupby('Category').agg({'Quantity':['sum', 'max'], 'Price':['mean']})
print(grouped_by_category)


#  Identify the top-selling product in each category based on the total quantity sold.
top_selling = sales.groupby(['Category', 'Product']).agg({'Quantity':'sum'})
most_sold = top_selling.sort_values(by='Quantity', ascending=False).groupby('Category').head(1)
print(most_sold)

#  Find the date on which the highest total sales (quantity * price) occurred.
sales['Total_Sales'] = sales['Quantity'] * sales['Price']
max_sales = sales['Total_Sales'].max()
result = sales[sales['Total_Sales'] == max_sales]
print(result[['Date', 'Total_Sales']])



"""
Homework Assignment 2: Examining Customer Orders
"""
# Group the data by CustomerID and filter out customers who have made less than 20 orders.
orders = pd.read_csv(r'C:\Python\lesson-19\homework\customer_orders.csv')
filtered = orders.groupby('CustomerID').filter(lambda x: len(x) < 20)
print(filtered)


# Identify customers who have ordered products with an average price per unit greater than $120.
average_price_per_customer = orders.groupby('CustomerID').agg({'Price':'mean'})
filterd_customers = average_price_per_customer[average_price_per_customer["Price"] > 120]
print(filterd_customers)

# Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 units.

total = orders.groupby('Product').agg({'Quantity':'sum', 'Price':'sum'})
print(total[total['Quantity'] < 5])


"""Homework Assignment 3: Population Salary Analysis

"task\population.db" sqlite database has population table.
"task\population salary analysis.xlsx" file defines Salary Band categories.
Read the data from population table and calculate following measures:
Percentage of population for each salary category;
Average salary in each salary category;
Median salary in each salary category;
Number of population in each salary category;
Calculate the same measures in each State"""


