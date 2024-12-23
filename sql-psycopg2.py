import psycopg2


# Connect to 'chinook' db
connection = psycopg2.connect(database="chinook")

# Build a cursor object of the database
cursor = connection.cursor()

# Fetch the results (multiple)
results = cursor.fetchall()

# Fetch the results (single)
#results = cursor.fetchone()

# Close the connection
connection.close()

# Print results
for result in results:
    print(result);