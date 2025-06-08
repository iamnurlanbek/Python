"""Homework 1:

import pandas as pd

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} df = pd.DataFrame(data)

Rename column names using function. "First Name" --> "first_name", "Age" --> "age
Print the first 3 rows of the DataFrame
Find the mean age of the individuals
Select and print only the 'Name' and 'City' columns
Add a new column 'Salary' with random salary values
Display summary statistics of the DataFrame
"""

import pandas as pd

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 
    'Age': [25, 30, 35, 40], 
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 
df = pd.DataFrame(data)


# Rename column names using function. "First Name" --> "first_name", "Age" --> "age
df = df.rename(columns={'First Name': 'first_name', 'Age':'age'})
print('\nRenaming columns:\n',df)

# Print the first 3 rows of the DataFrame
print("\nFirts 3 rows:\n", df.head(3))

# Find the mean age of the individuals
mean_age = df['age'].mean()
print("\nMean age is\n", mean_age)

# Select and print only the 'Name' and 'City' columns
name_city_columns = df[['first_name', 'City']]
print('\nName and City columns:\n', name_city_columns)

# Add a new column 'Salary' with random salary values
import numpy as np
salary = np.random.randint(1000, 50000, 4)
df['Salary'] = salary
print("\nFull DataFrame with Salary:\n", df)


# Display summary statistics of the DataFrame
summary_stat  = df.describe()
print('\nSummary Sitatistics:\n', summary_stat)

"""Homework 2:

Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', representing monthly sales and expenses data. Use below table.
Month	Sales	Expenses
Jan	5000	3000
Feb	6000	3500
Mar	7500	4000
Apr	8000	4500
Calculate and display the maximum sales and expenses.
Calculate and display the minimum sales and expenses.
Calculate and display the average sales and expenses."""

import pandas as pd

data = {
    "Month":['Jan', 'Feb', 'Mar', 'Apr'],
    "Sales":[5000, 6000, 7500, 8000],
    "Expenses":[3000, 3500, 4000, 4500],
}
sales_and_expenses = pd.DataFrame(data)
print('Sales and Expenses Dataframe:\n', sales_and_expenses)


# Calculate and display the maximum sales and expenses.
max_sales = sales_and_expenses['Sales'].max()
max_expenses= sales_and_expenses['Expenses'].max()

print('Max Sales:', max_sales)
print('Max Expenses:', max_expenses)


# Calculate and display the minimum sales and expenses.
min_sales = sales_and_expenses['Sales'].min()
min_expenses= sales_and_expenses['Expenses'].min()

print('Min Sales:', min_sales)
print('Min Expenses:', min_expenses)

# Calculate and display the average sales and expenses.
avg_sales = sales_and_expenses['Sales'].mean()
avg_expenses= sales_and_expenses['Expenses'].mean()

print('Avg Sales:', avg_sales)
print('Avg Expenses:', avg_expenses)


"""Homework 3:

Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', representing monthly expenses for different categories. Use below table.
Category	January	February	March	April
Rent	1200	1300	1400	1500
Utilities	200	220	240	250
Groceries	300	320	330	350
Entertainment	150	160	170	180
Calculate and display the maximum expense for each category.
Calculate and display the minimum expense for each category.
Calculate and display the average expense for each category.
In this task, use .set_index method to make Category column as index.

Try this code, learn it and use it in the task."""
import pandas as pd

data = {
    'Category':['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January':[1200, 200, 300, 150],
    'February':[1300, 220, 320, 160],
    'March':[1400, 240, 330, 170],
    'January':[1500, 250, 350, 180],
}

expenses = pd.DataFrame(data)
expenses.set_index('Category', inplace=True)
print('Expenses DataFrame:\n',expenses)

# Calculate and display the maximum expense for each category.
max_values = expenses.max(axis=1)
print(f"Max expense for each category:\n{max_values}")

# Calculate and display the minimum expense for each category.
min_values = expenses.min(axis=1)
print(f"Min expense for each category:\n{min_values}")

# Calculate and display the average expense for each category.
mean_values = expenses.mean(axis=1)
print('Mean expense for each category:\n', mean_values)

