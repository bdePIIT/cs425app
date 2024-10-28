from DBSetup import DBSetup


def main_menu():
    print("\n\n========================================")
    print("🚗 Parking Lots and Vehicles Management")
    print("========================================")
    print("|                                      |")
    print("|   [1] Manage Parking Lots            |")
    print("|   [2] Manage Vehicles                |")
    print("|   [3] Exit                           |")
    print("|                                      |")
    print("========================================")
    return input("Select an option: ").strip()


def parking_lot_menu():
    print("\n\n========================================")
    print("🅿️  Parking Lot Management")
    print("========================================")
    print("|                                      |")
    print("|   [1] Add Parking Lot                |")
    print("|   [2] View Parking Lots              |")
    print("|   [3] Update Parking Lot             |")
    print("|   [4] Delete Parking Lot             |")
    print("|   [5] Back to Main Menu              |")
    print("|                                      |")
    print("========================================")
    return input("Select an option: ").strip()


def vehicle_menu():
    print("\n\n========================================")
    print("🚙 Vehicle Management")
    print("========================================")
    print("|                                      |")
    print("|   [1] Add Vehicle                    |")
    print("|   [2] View Vehicles                  |")
    print("|   [3] Update Vehicle                 |")
    print("|   [4] Delete Vehicle                 |")
    print("|   [5] Back to Main Menu              |")
    print("|                                      |")
    print("========================================")
    return input("Select an option: ").strip()


def add_parking_lot(db):
    try:
        name = input("Enter parking lot name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")

        street = input("Enter street: ").strip()
        if not street:
            raise ValueError("Street cannot be empty.")

        city = input("Enter city: ").strip()
        if not city:
            raise ValueError("City cannot be empty.")

        state = input("Enter state (2-letter code): ").strip().upper()
        if len(state) != 2 or not state.isalpha():
            raise ValueError("State must be a 2-letter alphabetical code.")

        zip_code = input("Enter ZIP code: ").strip()
        if not zip_code.isdigit() or len(zip_code) != 5:
            raise ValueError("ZIP code must be a 5-digit number.")

        capacity = input("Enter capacity: ").replace(",", "").strip()
        if not capacity.isdigit() or int(capacity) <= 0:
            raise ValueError("Capacity must be a positive integer.")

        # Insert parking lot into database
        db.cursor.execute(
            """
            INSERT INTO parking_lots (name, street, city, state, zip_code, capacity)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (name, street, city, state, zip_code, int(capacity)),
        )
        db.connection.commit()
        print("Parking lot added successfully.")

    except Exception as e:
        print(f"{e}")


def view_parking_lots(db):
    try:
        db.cursor.execute("SELECT * FROM parking_lots")
        rows = db.cursor.fetchall()

        if rows:
            print(
                "\n==================================================================================="
            )
            print(
                "                              Parking Lots List                                    "
            )
            print(
                "==================================================================================="
            )
            print(
                f"{'ID':<5} {'Name':<20} {'Street':<20} {'City':<15} {'State':<7} {'ZIP':<7} {'Capacity':<10}"
            )
            print(
                "-----------------------------------------------------------------------------------"
            )

            for row in rows:
                parking_lot_id, name, street, city, state, zip_code, capacity = row
                print(
                    f"{parking_lot_id:<5} {name:<20} {street:<20} {city:<15} {state:<7} {zip_code:<7} {capacity:<10}"
                )

            print(
                "==================================================================================="
            )
        else:
            print("\nNo parking lots found in the database.")

    except Exception as e:
        print(f"{e}")


def update_parking_lot(db):
    try:
        # Validate parking lot ID input
        parking_lot_id = input("Enter parking lot ID to update: ").strip()
        if not parking_lot_id.isdigit():
            raise ValueError("Parking lot ID must be a valid integer.")

        # Check if the parking lot exists
        db.cursor.execute(
            "SELECT * FROM parking_lots WHERE parking_lot_id = ?", (parking_lot_id,)
        )
        if db.cursor.fetchone() is None:
            print("No parking lot found with the specified ID.")
            return  # Exit the function if the parking lot does not exist

        # Validate column input
        column = input(
            "Enter column to update (name, street, city, state, zip_code, capacity): "
        ).strip()
        valid_columns = {"name", "street", "city", "state", "zip_code", "capacity"}
        if column not in valid_columns:
            raise ValueError(
                f"Invalid column '{column}'. Please choose from {', '.join(valid_columns)}."
            )

        # Validate value based on column
        value = input("Enter new value: ").strip()
        if column == "state":
            if len(value) != 2 or not value.isalpha():
                raise ValueError("State must be a 2-letter alphabetical code.")
        elif column == "zip_code":
            if not value.isdigit() or len(value) != 5:
                raise ValueError("ZIP code must be a 5-digit number.")
        elif column == "capacity":
            value = value.replace(",", "").strip()  # Remove commas if any
            if not value.isdigit() or int(value) <= 0:
                raise ValueError("Capacity must be a positive integer.")
            value = int(value)  # Convert to integer for database insertion

        # Update parking lot in the database
        db.cursor.execute(
            f"UPDATE parking_lots SET {column} = ? WHERE parking_lot_id = ?",
            (value, parking_lot_id),
        )
        db.connection.commit()
        print("Parking lot updated successfully.")

    except Exception as e:
        print(f"{e}")


def delete_parking_lot(db):
    try:
        parking_lot_id = input("Enter parking lot ID to delete: ").strip()

        # Ensure parking_lot_id is a valid integer
        if not parking_lot_id.isdigit():
            raise ValueError("Parking lot ID must be a valid integer.")

        # Execute delete command
        db.cursor.execute(
            "DELETE FROM parking_lots WHERE parking_lot_id = ?", (parking_lot_id,)
        )
        db.connection.commit()

        # Check if a row was actually deleted
        if db.cursor.rowcount == 0:
            print("No parking lot found with the specified ID.")
        else:
            print("Parking lot deleted successfully.")

    except Exception as e:
        print(f"{e}")


def add_vehicle(db):
    try:
        # Validate license plate input
        license_plate = input("Enter vehicle license plate: ").strip()
        if not license_plate:
            raise ValueError("License plate cannot be empty.")

        # Validate state input
        state = input("Enter vehicle state (2-letter code): ").strip().upper()
        if len(state) != 2 or not state.isalpha():
            raise ValueError("State must be a 2-letter alphabetical code.")

        # Collect other details without specific validation
        color = input("Enter vehicle color: ").strip()
        make = input("Enter vehicle make: ").strip()
        model = input("Enter vehicle model: ").strip()

        # Validate and check parking lot ID
        parking_lot_id = input(
            "Enter parking lot ID where the vehicle is parked: "
        ).strip()
        if not parking_lot_id.isdigit():
            raise ValueError("Parking lot ID must be a valid integer.")

        # Check if the parking lot exists
        db.cursor.execute(
            "SELECT * FROM parking_lots WHERE parking_lot_id = ?", (parking_lot_id,)
        )
        if db.cursor.fetchone() is None:
            print("No parking lot found with the specified ID.")
            return  # Exit if the parking lot doesn't exist

        # Insert vehicle into the database
        db.cursor.execute(
            """
            INSERT INTO vehicles (license_plate, state, color, make, model, parking_lot_id)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (license_plate, state, color, make, model, int(parking_lot_id)),
        )
        db.connection.commit()
        print("Vehicle added successfully.")

    except Exception as e:
        print(f"{e}")


def view_vehicles(db):
    try:
        db.cursor.execute("SELECT * FROM vehicles")
        rows = db.cursor.fetchall()

        if rows:
            print("\n=====================================")
            print("           Vehicles List             ")
            print("=====================================")
            print(
                f"{'ID':<5} {'License Plate':<15} {'State':<7} {'Color':<10} {'Make':<10} {'Model':<10} {'Parking Lot ID':<15}"
            )
            print(
                "--------------------------------------------------------------------------"
            )

            for row in rows:
                vehicle_id, license_plate, state, color, make, model, parking_lot_id = (
                    row
                )
                print(
                    f"{vehicle_id:<5} {license_plate:<15} {state:<7} {color:<10} {make:<10} {model:<10} {parking_lot_id:<15}"
                )

            print("=====================================")
        else:
            print("\nNo vehicles found in the database.")

    except Exception as e:
        print(f"{e}")


def update_vehicle(db):
    try:
        # Validate license plate input
        license_plate = input("Enter vehicle license plate to update: ").strip()
        if not license_plate:
            raise ValueError("License plate cannot be empty.")

        # Check if the vehicle exists
        db.cursor.execute(
            "SELECT * FROM vehicles WHERE license_plate = ?", (license_plate,)
        )
        if db.cursor.fetchone() is None:
            print("No vehicle found with the specified license plate.")
            return  # Exit the function if the vehicle does not exist

        # Validate column input
        column = input(
            "Enter column to update (state, color, make, model, parking_lot_id): "
        ).strip()
        valid_columns = {"state", "color", "make", "model", "parking_lot_id"}
        if column not in valid_columns:
            raise ValueError(
                f"Invalid column '{column}'. Please choose from {', '.join(valid_columns)}."
            )

        # Validate value based on column
        value = input("Enter new value: ").strip()
        if column == "state":
            if len(value) != 2 or not value.isalpha():
                raise ValueError("State must be a 2-letter alphabetical code.")
        elif column == "parking_lot_id":
            if not value.isdigit():
                raise ValueError("Parking lot ID must be a valid integer.")
            value = int(value)  # Convert to integer for database insertion

        # Update vehicle in database
        db.cursor.execute(
            f"UPDATE vehicles SET {column} = ? WHERE license_plate = ?",
            (value, license_plate),
        )
        db.connection.commit()
        print("Vehicle updated successfully.")

    except Exception as e:
        print(f"{e}")


def delete_vehicle(db):
    try:
        # Validate license plate input
        license_plate = input("Enter vehicle license plate to delete: ").strip()
        if not license_plate:
            raise ValueError("License plate cannot be empty.")

        # Execute delete command
        db.cursor.execute(
            "DELETE FROM vehicles WHERE license_plate = ?", (license_plate,)
        )
        db.connection.commit()

        # Check if a row was actually deleted
        if db.cursor.rowcount == 0:
            print("No vehicle found with the specified license plate.")
        else:
            print("Vehicle deleted successfully.")

    except Exception as e:
        print(f"{e}")


def main():
    db = DBSetup()  # Set up the database

    while True:
        choice = main_menu()

        if choice == "1":
            while True:
                lot_choice = parking_lot_menu()

                if lot_choice == "1":
                    add_parking_lot(db)
                elif lot_choice == "2":
                    view_parking_lots(db)
                elif lot_choice == "3":
                    update_parking_lot(db)
                elif lot_choice == "4":
                    delete_parking_lot(db)
                elif lot_choice == "5":
                    break
                else:
                    print("\nInvalid option. Please try again.")

        elif choice == "2":
            while True:
                vehicle_choice = vehicle_menu()

                if vehicle_choice == "1":
                    add_vehicle(db)
                elif vehicle_choice == "2":
                    view_vehicles(db)
                elif vehicle_choice == "3":
                    update_vehicle(db)
                elif vehicle_choice == "4":
                    delete_vehicle(db)
                elif vehicle_choice == "5":
                    break
                else:
                    print("\nInvalid option. Please try again.")

        elif choice == "3":
            print("Exiting application.")
            break
        else:
            print("\nInvalid option. Please try again.")

    db.disconnect()  # Close the database connection


if __name__ == "__main__":
    main()
