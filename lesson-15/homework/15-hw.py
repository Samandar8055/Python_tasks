## Review Lesson_15
# Task 1

'''Create a new database with a table named Roster that has three fields: Name, Species, and Age.
 The Name and Species columns should be text fields, and the Age column should be an integer field.'''
import sqlite3

# Connect to database (creates file if it doesn't exist)
conn = sqlite3.connect("roster.db")

# Create a cursor
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# Save changes and close
conn.commit()
conn.close()

print("✅ Database and Roster table created successfully")

# Task 2
import sqlite3

# Connect to database
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

# Insert data
cursor.execute(
    "INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)",
    ("Benjamin Sisko", "Human", 40)
)

cursor.execute(
    "INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)",
    ("Jadzia Dax", "Trill", 300)
)

cursor.execute(
    "INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)",
    ("Kira Nerys", "Bajoran", 29)
)

# Save changes and close
conn.commit()
conn.close()

print("✅ Data inserted successfully")

# Task 3
import sqlite3

# Connect to database
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

# Update record
cursor.execute(
    "UPDATE Roster SET Name = ? WHERE Name = ?",
    ("Ezri Dax", "Jadzia Dax")
)

# Save changes and close
conn.commit()
conn.close()

print("✅ Name updated successfully")

# task 4
import sqlite3

# Connect to database
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

# Select Bajoran records
cursor.execute(
    "SELECT Name, Age FROM Roster WHERE Species = ?",
    ("Bajoran",)
)

results = cursor.fetchall()

# Print results
for name, age in results:
    print("Name:", name, "| Age:", age)

conn.close()
