"""DataFrame 1: Student Grades
import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)
Exercise 1: Calculate the average grade for each student.

Exercise 2: Find the student with the highest average grade.

Exercise 3: Create a new column 'Total' representing the total marks obtained by each student.

Exercise 4: Plot a bar chart to visualize the average grades in each subject.
"""

import pandas as pd
import matplotlib.pyplot as plt

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

student = pd.DataFrame(data1)

# Exercise 1: Calculate the average grade for each student.
student['Average Grade'] = student[['Math', 'English', 'Science']].apply(lambda row: row.mean(), axis=1)
average_grade_by_student = student[['Student_ID', 'Average Grade']]
print(average_grade_by_student)

#  Exercise 2: Find the student with the highest average grade.
highest_average_grade_by_student = student.sort_values('Average Grade', ascending=False).head(1)
print(highest_average_grade_by_student)


#  Exercise 3: Create a new column 'Total' representing the total marks obtained by each student.
student['Total'] = student[['Math', 'English', 'Science']].sum(axis=1)
total_marks_by_student = student[['Student_ID', 'Total']]
print(total_marks_by_student)


# Exercise 4: Plot a bar chart to visualize the average grades in each subject.
average_grade_by_subject = student[['Math', 'English', 'Science']].mean()

average_grade_by_subject.plot(
    kind='bar',
    figsize=(10, 6),
    colormap='Set2',
    width=0.8,
    alpha=0.8,
    title='Average Grade by Subject',
)

plt.xlabel('Subject')
plt.ylabel('Average Grade')
plt.tight_layout()
plt.show()


"""
DataFrame 2: Sales Data
import pandas as pd

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)
Exercise 1: Calculate the total sales for each product.

Exercise 2: Find the date with the highest total sales.

Exercise 3: Calculate the percentage change in sales for each product from the previous day.

Exercise 4: Plot a line chart to visualize the sales trends for each product over time.

DataFrame 3: Employee Information
"""
data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}
sales = pd.DataFrame(data2)
# print(sales)

# Exercise 1: Calculate the total sales for each product.
total_sales = sales[['Product_A', 'Product_B', 'Product_C']].sum().reset_index()
total_sales.columns = ['Product', 'Total Sales']
print(total_sales)


# Exercise 2: Find the date with the highest total sales.
# print(sales)
sales['Total Sales'] = sales[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
result = sales.sort_values(['Total Sales'], ascending=[False]).head(2)
print(result[['Date', 'Total Sales']])

# Exercise 3: Calculate the percentage change in sales for each product from the previous day.
sales['Day'] = sales['Date'].dt.day_name()
sales['Total Sales'] = sales[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
sales['Percentage Change'] = sales['Total Sales'].pct_change() * 100
sales['Percentage Change'] = sales['Percentage Change'].fillna(0)
print(sales)


# Exercise 4: Plot a line chart to visualize the sales trends for each product over time.

# Daily Trend
sales['Day'] = sales['Date'].dt.day_name()
daily_trend = sales.groupby('Day')['Total Sales'].sum()
daily_trend.plot(
    kind='line',
    ls='-.',
    lw=2,
    figsize=(10, 6),
    marker='X',
    markersize=6,
)

plt.title('Daily Trend')
plt.xlabel('Name of Days')
plt.ylabel('Total Sales')
plt.grid()
plt.legend()
plt.show()

print(daily_trend)

#  Monthly Trend
sales['Month'] = sales['Date'].dt.month_name()
monthly_trend = sales.groupby('Month')['Total Sales'].sum()
monthly_trend.plot(
    kind='line',
    ls='-.',
    figsize=(10, 6),
    marker='X',
    markersize=6,

)

plt.title('Monthly Trend')
plt.xlabel('Month')
plt.ylabel('Total Revenue (3177)')
plt.legend()
plt.tight_layout()
plt.grid()
plt.show()

print(monthly_trend)


#  Yearly Trend
sales['Year'] = sales['Date'].dt.year
yearly_trend = sales.groupby('Year')['Total Sales'].sum()
yearly_trend.plot(
    kind='line',
    figsize=(10, 6),
    ls='-.',
    lw=2,
    marker='X',
    markersize=6,
    )

plt.title('Chiziqli Grafik')
plt.xlabel('Year(2023)')
plt.ylabel('Total Sales (3177)')
plt.grid()
plt.tight_layout()
plt.show()
print(yearly_trend)


"""
DataFrame 3: Employee Information
import pandas as pd

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)
Exercise 1: Calculate the average salary for each department.

Exercise 2: Find the employee with the most experience.

Exercise 3: Create a new column 'Salary Increase' representing the percentage increase in salary from the minimum salary in the dataframe.

Exercise 4: Plot a bar chart to visualize the distribution of employees across different departments.
"""

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}
employees = pd.DataFrame(data3)

# Exercise 1: Calculate the average salary for each department.
average_salary_by_department = employees.groupby(by='Department').agg({'Salary':'mean'}).reset_index().rename(columns={'Salary':'Average Salary'})
print(average_salary_by_department)


# Exercise 2: Find the employee with the most experience.
most_exprience_employee = employees.sort_values('Experience (Years)', ascending=False).head(1)
print(most_exprience_employee)


# Exercise 3: Create a new column 'Salary Increase' representing the percentage increase in salary from the minimum salary in the dataframe.
employees = employees.sort_values('Salary')
employees['Salary Increase (%)'] =  employees['Salary'].pct_change() * 100
print(employees)


# Exercise 4: Plot a bar chart to visualize the distribution of employees across different departments.
employees_by_department = employees.groupby('Department').agg({'Employee_ID':'count'})
employees_by_department.plot(
    kind='bar',
    figsize=(10, 6),
    colormap='Set2',
    edgecolor='black',
    width=0.8,
    alpha=0.9,
    title='Bar Chart',

)
plt.xlabel('Department')
plt.ylabel('Employees Count')
plt.legend()
plt.grid(axis='y')
plt.show()



"""ataFrame 4: Customer Orders
import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)
Exercise 1: Calculate the total revenue from all orders.

Exercise 2: Find the most ordered product.

Exercise 3: Calculate the average quantity of products ordered.

Exercise 4: Plot a pie chart to visualize the distribution of sales across different products."""

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

orders = pd.DataFrame(data4)


# Exercise 1: Calculate the total revenue from all orders.
total_revenue = orders['Total_Price'].sum()
summary = pd.Series({'Total Revenue':total_revenue})
print(summary)


# Exercise 2: Find the most ordered product.
ordered_product = orders.groupby('Product')['Quantity'].sum().reset_index()
most_ordered_product = ordered_product.sort_values('Quantity', ascending=False).head(1)
print(most_ordered_product)


# Exercise 3: Calculate the average quantity of products ordered
average_quantity = orders['Quantity'].mean()
result = pd.Series({'Average Quantity':average_quantity})
print(result)


# Exercise 4: Plot a pie chart to visualize the distribution of sales across different products.

products = pd.pivot_table(orders, index='Product', values='Quantity', aggfunc='sum')
products.plot(
    kind='pie',
    figsize=(10, 6),
    subplots=True,
    startangle=90,
    autopct='%1.1f%%',
    shadow=True,
)

plt.title('Sales Distribution by Product')
plt.axis('equal')
plt.tight_layout()
plt.legend()
plt.show()



