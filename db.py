
import mysql.connector

# Define the database connection parameters
username = 'your_username'
password = 'your_password'
host = 'your_host'
database = 'your_database'

# Create a connection to the database
conn = mysql.connector.connect(
    user=username,
    password=password,
    host=host,
    database=database
)

# Create a cursor object
cursor = conn.cursor()