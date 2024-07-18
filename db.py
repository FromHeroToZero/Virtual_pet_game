# Import the sqlite3 module to interact with the SQLite database
import sqlite3

from pet import Pet


# Define the DatabaseManager class to handle all database operations
class DatabaseManager:
    # Initialize the DatabaseManager with a database name
    def __init__(self, name="pet_data.db"):
        # Establish a connection to the SQLite database
        self.connection = sqlite3.connect(name)

        # Create the pet table if it doesn't exist
        self.create_table()

    def create_table(self):
        c = self.connection.cursor()
        c.execute('''
         CREATE TABLE IF NOT EXISTS pet
         (name TEXT, hunger INTEGER, happiness INTEGER, cleanliness INTEGER) 
         ''')
        self.connection.commit()

    # Close the database connection
    def close(self):
        # Close the connection to the database
        self.conn.close()

    # Load the pet's data from the database
    def load_pet(self, pet: Pet):
        # Create a cursor object to execute SQL commands
        c = self.connection.cursor()
        # Execute the SQL command to select all data from the pet table
        c.execute('SELECT * FROM pet')
        # Fetch one row of results from the query
        row = c.fetchone()
        if row:
            # If a row is found, unpack the data into the pet's attributes
            pet.name, pet.hunger, pet.happiness, pet.cleanliness = row
            print(f"{pet.name}'s data has been loaded.")
            return pet
        else:
            print("No saved data found.")

    # Create method to save the pet's data to the database
    def save_pet(self, pet: Pet):
        # Create a cursor object to execute SQL commands
        c = self.connection.cursor()
        # Delete existing data from the pet table
        c.execute('DELETE FROM pet')
        # Insert the pet's data into the pet table
        c.execute('INSERT INTO pet VALUES (?, ?, ?, ?)', (pet.name, pet.hunger, pet.happiness, pet.cleanliness))
        # Commit the transaction to save the changes to the database
        self.connection.commit()
        # Print a message indicating that the pet's data has been saved
        print(f"{pet.name}'s data has been saved.")

# Create the pet table in the database
# Create a cursor object to execute SQL commands
# Execute the SQL command to create the pet table
# Commit the transaction to save the changes to the database

# Close the database connection
# Close the connection to the database



