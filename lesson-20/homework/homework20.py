
"""Homework 1:

Using chinook.db write pandas code.

Customer Purchases Analysis:
Find the total amount spent by each customer on purchases (considering invoices).
Identify the top 5 customers with the highest total purchase amounts.
Display the customer ID, name, and the total amount spent for the top 5 customers.
Album vs. Individual Track Purchases:
Determine the percentage of customers who prefer to buy individual tracks instead of full albums.
A customer is considered to prefer individual tracks if they have purchased only a subset of tracks from an album.
Provide a summary of the percentage of customers who fall into each category (individual tracks vs. full albums).
"""


import sqlite3
import pandas as pd

conn = sqlite3.connect(r'C:\Python\lesson-20\homework\chinook.db')
inovices_query = 'Select * from invoices'
customers_query = 'Select CustomerId, FirstName, LastName from customers'
invoices = pd.read_sql_query(inovices_query, conn)
customers = pd.read_sql_query(customers_query, conn)

# Find the total amount spent by each customer on purchases (considering invoices).
total_amount_by_customer = pd.pivot_table(invoices, index='CustomerId', values='Total', aggfunc='sum').reset_index()
total_amount_by_customer.columns = ['CustomerId', 'Total Purchases']
# print(total_amount_by_customer)


# Identify the top 5 customers with the highest total purchase amounts.
total_by_customer = pd.pivot_table(invoices, index='CustomerId', values='Total', aggfunc='sum').reset_index()
total_by_customer.columns = ['CustomerId', 'Total Purchases']
top_five_customers = total_by_customer.sort_values(['Total Purchases'], ascending=[False]).head(5)
# print(top_five_customers)


# Display the customer ID, name, and the total amount spent for the top 5 customers.
total_by_customer = pd.pivot_table(invoices, index='CustomerId', values='Total', aggfunc='sum').reset_index()
total_by_customer.columns = ['CustomerId', 'TotalPurchases']
top_five_customers = total_by_customer.sort_values(['TotalPurchases'], ascending=[False]).head(5)
top_five_customers = top_five_customers.merge(customers, how='left', on='CustomerId')
# print(top_five_customers)


# Determine the percentage of customers who prefer to buy individual tracks instead of full albums.
query = """
SELECT ii.InvoiceId, i.CustomerId, ii.TrackId, t.AlbumId
FROM invoice_items ii
JOIN invoices i ON i.InvoiceId = ii.InvoiceId
JOIN tracks t ON t.TrackId = ii.TrackId
"""

df = pd.read_sql_query(query, conn)


album_track_counts = df.groupby('AlbumId')['TrackId'].nunique().reset_index()
album_track_counts.columns = ['AlbumId', 'TotalTracks']



customer_album_purchases = df.groupby(['CustomerId', 'AlbumId'])['TrackId'].nunique().reset_index()
customer_album_purchases.columns = ['CustomerId', 'AlbumId', 'PurchasedTracks']



merged = pd.merge(customer_album_purchases, album_track_counts, on='AlbumId')


merged['is_album_purchase'] = merged['PurchasedTracks'] == merged['TotalTracks']


customer_type = merged.groupby('CustomerId')['is_album_purchase'].any().reset_index()
customer_type['CustomerType'] = customer_type['is_album_purchase'].apply(lambda x: 'Album Buyer' if x else 'Track Buyer')

total_customers = customer_type['CustomerId'].nunique()
summary = customer_type['CustomerType'].value_counts(normalize=True) * 100
print(summary)
