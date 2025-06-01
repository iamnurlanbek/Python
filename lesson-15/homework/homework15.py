"""Create a new database with a table named Roster that has three fields: Name, Species, and Age. 
The Name and Species columns should be text fields, and the Age column should be an integer field.
Populate your new table with the following values:
Name	Species	Age
Benjamin Sisko	Human	40
Jadzia Dax	Trill	300
Kira Nerys	Bajoran	29
Update the Name of Jadzia Dax to be Ezri Dax
Display the Name and Age of everyone in the table classified as Bajoran."""

import sqlite3

connection = sqlite3.connect(r"C:\Python\lesson-15\homework\mydb.db")
my_cursor = connection.cursor()

# Creating table
my_cursor.execute("""
                    CREATE TABLE Roster (
                        Name TEXT,
                        Species TEXT,
                        Age INTEGER
                    )              

""")

# Insert values into table
my_cursor.execute("""INSERT INTO Roster (Name, Species, Age) values 
                  ('Benjamin Sisko', 'Human', 40), 
                  ('Jadzia Dax', 'Trill', 300), 
                  ('Kira Nerys', 'Bajoran', 29)
            """)


# Updating name
my_cursor.execute("""
                  UPDATE  Roster
                  SET Name = 'Ezri Dax' 
                  WHERE Name = 'Jadzia Dax'
            """)

# Displaying value
result = my_cursor.execute("""
                  SELECT Name, Age FROM Roster
                  WHERE Species = 'Bajoran'
            """)

for r in result.fetchall():
    print(f"Name: {r[0]}\nAge: {r[1]}")
    
    
connection.commit()
connection.close()

