import sqlite3

connection = sqlite3.connect("lesson-13/homework/library.db")

cursor = connection.cursor()

# cursor.execute("""
#     CREATE TABLE Books (
#         Title TEXT,
#         Author TEXT,
#         Year_Published INT,
#         GENRE TEXT)""")



# cursor.execute("INSERT INTO Books (Title, Author, Year_Published, GENRE) VALUES (?, ?, ?, ?)", ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"))
# cursor.execute("INSERT INTO Books (Title, Author, Year_Published, GENRE) VALUES (?, ?, ?, ?)", ("1984", "George Orwell", 1949, "Dystopian"))
# cursor.execute("INSERT INTO Books (Title, Author, Year_Published, GENRE) VALUES (?, ?, ?, ?)", ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic"))


# cursor.execute("UPDATE Books SET Year_Published = ? WHERE Title = ?", (1950, "1984"))


# Retrieve and display the Title and Author of all books where the Genre is Dystopian.
# cursor.execute("SELECT Title, Author FROM Books WHERE GENRE = ?", ("Dystopian",))
# res = cursor.fetchall()
# for i in res:
#     print(i)


# cursor.execute("DELETE FROM Books WHERE Year_Published < 1950")

# cursor.execute("ALTER TABLE Books ADD COLUMN Rating FLOAT;")
# cursor.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (4.8, "To Kill a Mockingbird"))
# cursor.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (4.7, "1984"))
# cursor.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (4.5, "The Great Gatsby"))

cursor.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
res = cursor.fetchall()
for j in res:
    print(j)

connection.commit()
connection.close()