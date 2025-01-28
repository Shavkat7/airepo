import sqlite3

connection = sqlite3.connect("lesson-13/homework/roster.db")

cursor = connection.cursor()

# cursor.execute(""" 
#     CREATE TABLE Roster (
#         Name TEXT, 
#         Species TEXT,
#         Age INT)""")


# cursor.execute("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", ("Benjamin Sisko", "Human", 40))
# cursor.execute("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", ("Jadzia Dax", "Trill", 300))
# cursor.execute("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", ("Kira Nerys", "Bajoran", 29))

# cursor.execute("UPDATE Roster SET Name = ? Where Name = ?", ("Ezri Dax", "Jadzia Dax"))

# cursor.execute("SELECT Name, Age FROM Roster WHERE Species = ?", ("Bajoran",))
# results = cursor.fetchall()
# for row in results:
    # print(f"Name: {row[0]}, Age: {row[1]}")

# cursor.execute("DELETE FrOm roster where Age > 100")

# cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT;")
# cursor.execute("UPDATE Roster SET Rank = ? WHERE Name = ?", ("Captain", "Benjamin Sisko"))
# cursor.execute("UPDATE Roster SET Rank = ? WHERE Name = ?", ("Major", "Kira Nerys"))

# Retrieve all characters sorted by their Age in descending order.
cursor.execute("SELECT * FROM Roster ORDER BY Age DESC")
res = cursor.fetchall()
for r in res:
    print(r)

connection.commit()
connection.close()