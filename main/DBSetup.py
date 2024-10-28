import sqlite3
import os


class DBSetup:
    def __init__(self, db_path="resources/ParkingLotDB.db"):
        self.db_path = db_path
        self.connection = None
        self.cursor = None
        self.connect()  # Automatically connect on initialization
        self.create_tables()

    def connect(self):
        # Ensure the 'resources' folder exists
        if not os.path.exists(os.path.dirname(self.db_path)):
            os.makedirs(os.path.dirname(self.db_path))

        # Connect to the SQLite database
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        print(f"Connected to database at {self.db_path}")

    def create_tables(self):
        # SQL for creating the parking_lots table
        create_parking_lots_table = """
        CREATE TABLE IF NOT EXISTS parking_lots (
            parking_lot_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            street TEXT NOT NULL,
            city TEXT NOT NULL,
            state TEXT NOT NULL,
            zip_code TEXT NOT NULL,
            capacity INTEGER NOT NULL
        );
        """

        # SQL for creating the vehicles table
        create_vehicles_table = """
        CREATE TABLE IF NOT EXISTS vehicles (
            vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
            license_plate TEXT UNIQUE NOT NULL,
            state TEXT NOT NULL,
            color TEXT,
            make TEXT,
            model TEXT,
            parking_lot_id INTEGER,
            FOREIGN KEY (parking_lot_id) REFERENCES parking_lots(parking_lot_id)
        );
        """

        # Execute SQL to create tables if they don't already exist
        self.cursor.execute(create_parking_lots_table)
        self.cursor.execute(create_vehicles_table)

        # Commit changes
        self.connection.commit()
        print("Tables created successfully.")

    def disconnect(self):
        # Close the database connection
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
