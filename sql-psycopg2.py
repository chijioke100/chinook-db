import psycopg2


# Connect to 'chinook' db
connection = psycopg2.connect(database="chinook")

# Build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
cursor.execute('SELECT * FROM "Artist"')

# Fetch the results (multiple)
results = cursor.fetchall()

# Fetch the results (single)
#results = cursor.fetchone()

# Close the connection
connection.close()

# Print results
for result in results:
    print(result);