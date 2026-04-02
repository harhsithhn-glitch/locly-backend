import sqlite3

# connect to database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# fetch all data
c.execute("SELECT * FROM bookings")
rows = c.fetchall()

# print data
for row in rows:
    print(row)

conn.close()