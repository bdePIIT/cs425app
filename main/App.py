from DBSetup import DBSetup


def main_menu():
    while True:
        print("\n\n========================================")
        print("🚗 Parking Lots and Vehicles Management")
        print("========================================")
        print("|                                      |")
        print("|   [1] Manage Parking Lots            |")
        print("|   [2] Manage Vehicles                |")
        print("|   [3] Calculate Available Spaces     |")
        print("|   [4] Rank Parking Lots by Cars      |")
        print("|   [5] OLAP - Stats on Car Makes      |")
        print("|   [6] Exit                           |")
        print("|                                      |")
        print("========================================")
        option = input("Select an option: ").strip()
        if option in ["1", "2", "3", "4", "5", "6"]:
            return option
        else:
            print("Invalid option. Please select a valid option from the menu.")


def parking_lot_menu():
    while True:
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
        option = input("Select an option: ").strip()
        if option in ["1", "2", "3", "4", "5"]:
            return option
        else:
            print("Invalid option. Please select a valid option from the menu.")


def vehicle_menu():
    while True:
        print("\n\n========================================")
        print("🚙 Vehicle Management")
        print("========================================")
        print("|                                      |")
        print("|   [1] Add Vehicle                    |")
        print("|   [2] View Vehicles                  |")
        print("|   [3] Update Vehicle                 |")
        print("|   [4] Delete Vehicle                 |")
        print("|   [5] Search Vehicles by Attribute   |")
        print("|   [6] Set Operations - Union         |")
        print("|   [7] Set Membership - Filter        |")
        print("|   [8] Set Comparison - Similar Cars  |")
        print("|   [9] Set With Subqueries - Common Attributes |")
        print("|   [10] Back to Main Menu             |")
        print("|                                      |")
        print("========================================")
        option = input("Select an option: ").strip()
        if option in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            return option
        else:
            print("Invalid option. Please select a valid option from the menu.")


def add_parking_lot(db):
    try:
        name = input("Enter parking lot name: ").strip()
        street = input("Enter street: ").strip()
        city = input("Enter city: ").strip()
        state = input("Enter state: ").strip()
        zip_code = input("Enter zip code: ").strip()
        capacity = int(input("Enter capacity: "))

        db.cursor.execute("INSERT INTO parking_lots (name, street, city, state, zip_code, capacity) VALUES (?, ?, ?, ?, ?, ?)",
                          (name, street, city, state, zip_code, capacity))
        db.connection.commit()
        print("Parking lot added successfully.")
    except Exception as e:
        print(f"An error occurred while adding the parking lot: {e}")


def add_vehicle(db):
    try:
        license_plate = input("Enter license plate: ").strip()
        state = input("Enter state: ").strip()
        color = input("Enter color: ").strip()
        make = input("Enter make: ").strip()
        model = input("Enter model: ").strip()
        parking_lot_id = input("Enter parking lot ID (or leave blank if none): ").strip()
        parking_lot_id = int(parking_lot_id) if parking_lot_id else None

        db.cursor.execute("INSERT INTO vehicles (license_plate, state, color, make, model, parking_lot_id) VALUES (?, ?, ?, ?, ?, ?)",
                          (license_plate, state, color, make, model, parking_lot_id))
        db.connection.commit()
        print("Vehicle added successfully.")
    except Exception as e:
        print(f"An error occurred while adding the vehicle: {e}")


def update_parking_lot(db):
    try:
        parking_lot_id = input("Enter the ID of the parking lot to update: ").strip()
        fields = {
            "1": "name",
            "2": "street",
            "3": "city",
            "4": "state",
            "5": "zip_code",
            "6": "capacity"
        }
        while True:
            print("Select the field to update:")
            print("[1] Name")
            print("[2] Street")
            print("[3] City")
            print("[4] State")
            print("[5] Zip Code")
            print("[6] Capacity")
            field_option = input("Enter the number of the field to update: ").strip()
            if field_option in fields:
                new_value = input(f"Enter new value for {fields[field_option]}: ").strip()
                if field_option == "6":  # Capacity is an integer
                    new_value = int(new_value)
                db.cursor.execute(f"UPDATE parking_lots SET {fields[field_option]} = ? WHERE parking_lot_id = ?",
                                  (new_value, parking_lot_id))
                db.connection.commit()
                print("Parking lot updated successfully.")
                break
            else:
                print("Invalid option selected. Please choose a valid field to update.")
    except Exception as e:
        print(f"An error occurred while updating the parking lot: {e}")


def delete_parking_lot(db):
    try:
        parking_lot_id = input("Enter the ID of the parking lot to delete: ").strip()
        db.cursor.execute("DELETE FROM parking_lots WHERE parking_lot_id = ?", (parking_lot_id,))
        db.connection.commit()
        print("Parking lot deleted successfully.")
    except Exception as e:
        print(f"An error occurred while deleting the parking lot: {e}")


def update_vehicle(db):
    try:
        vehicle_id = input("Enter the ID of the vehicle to update: ").strip()
        fields = {
            "1": "license_plate",
            "2": "state",
            "3": "color",
            "4": "make",
            "5": "model",
            "6": "parking_lot_id"
        }
        while True:
            print("Select the field to update:")
            print("[1] License Plate")
            print("[2] State")
            print("[3] Color")
            print("[4] Make")
            print("[5] Model")
            print("[6] Parking Lot ID")
            field_option = input("Enter the number of the field to update: ").strip()
            if field_option in fields:
                new_value = input(f"Enter new value for {fields[field_option]}: ").strip()
                if field_option == "6":  # Parking Lot ID is an integer
                    new_value = int(new_value) if new_value else None
                db.cursor.execute(f"UPDATE vehicles SET {fields[field_option]} = ? WHERE vehicle_id = ?",
                                  (new_value, vehicle_id))
                db.connection.commit()
                print("Vehicle updated successfully.")
                break
            else:
                print("Invalid option selected. Please choose a valid field to update.")
    except Exception as e:
        print(f"An error occurred while updating the vehicle: {e}")


def delete_vehicle(db):
    try:
        vehicle_id = input("Enter the ID of the vehicle to delete: ").strip()
        db.cursor.execute("DELETE FROM vehicles WHERE vehicle_id = ?", (vehicle_id,))
        db.connection.commit()
        print("Vehicle deleted successfully.")
    except Exception as e:
        print(f"An error occurred while deleting the vehicle: {e}")


def search_vehicle(db):
    try:
        while True:
            attribute_map = {
                "1": "license_plate",
                "2": "color",
                "3": "make",
                "4": "model"
            }
            attribute = input("Search by [1] License Plate, [2] Color, [3] Make, [4] Model: ").strip()
            if attribute in attribute_map:
                value = input("Enter search value: ").strip().lower()
                query = f"SELECT * FROM vehicles WHERE LOWER({attribute_map[attribute]}) = ?"
                results = db.cursor.execute(query, (value,)).fetchall()
                if results:
                    for vehicle in results:
                        print(f"Vehicle ID: {vehicle[0]}, License Plate: {vehicle[1]}, State: {vehicle[2]}, Color: {vehicle[3]}, Make: {vehicle[4]}, Model: {vehicle[5]}, Parking Lot ID: {vehicle[6]}")
                else:
                    print("No vehicles found matching the criteria.")
                break
            else:
                print("Invalid option. Please select a valid attribute to search by.")
    except Exception as e:
        print(f"An error occurred while searching for a vehicle: {e}")


def set_operations_union(db):
    try:
        print("Set Operations - Union")
        valid_attributes = ["color", "make", "model"]
        parking_lot_id_1 = input("Enter the ID of the first parking lot: ").strip()
        attribute_1 = input("Enter the attribute for the first parking lot (e.g., color, make, model): ").strip().lower()
        if attribute_1 not in valid_attributes:
            print("Invalid attribute. Please select a valid attribute (color, make, model).")
            return
        value_1 = input(f"Enter the value for {attribute_1} in the first parking lot: ").strip()

        parking_lot_id_2 = input("Enter the ID of the second parking lot: ").strip()
        attribute_2 = input("Enter the attribute for the second parking lot (e.g., color, make, model): ").strip().lower()
        if attribute_2 not in valid_attributes:
            print("Invalid attribute. Please select a valid attribute (color, make, model).")
            return
        value_2 = input(f"Enter the value for {attribute_2} in the second parking lot: ").strip()

        query = (
            "SELECT * FROM vehicles WHERE parking_lot_id = ? AND LOWER({}) = ? "
            "UNION "
            "SELECT * FROM vehicles WHERE parking_lot_id = ? AND LOWER({}) = ?"
        ).format(attribute_1, attribute_2)
        results = db.cursor.execute(query, (parking_lot_id_1, value_1.lower(), parking_lot_id_2, value_2.lower())).fetchall()

        if results:
            for vehicle in results:
                print(f"Vehicle ID: {vehicle[0]}, License Plate: {vehicle[1]}, State: {vehicle[2]}, Color: {vehicle[3]}, Make: {vehicle[4]}, Model: {vehicle[5]}, Parking Lot ID: {vehicle[6]}")
        else:
            print("No vehicles found matching the criteria.")
    except Exception as e:
        print(f"An error occurred while performing the set operation: {e}")


def set_membership_filter(db):
    try:
        print("Set Membership - Filter")
        valid_attributes = ["color", "make", "model"]
        attribute = input("Enter the attribute to filter by (e.g., color, make, model): ").strip().lower()
        if attribute not in valid_attributes:
            print("Invalid attribute. Please select a valid attribute (color, make, model).")
            return
        values = input(f"Enter the values to exclude for {attribute} (comma-separated): ").strip().split(',')
        values = [value.strip().lower() for value in values]
        placeholders = ', '.join('?' for _ in values)
        query = f"SELECT * FROM vehicles WHERE LOWER({attribute}) NOT IN ({placeholders})"
        results = db.cursor.execute(query, values).fetchall()

        if results:
            for vehicle in results:
                print(f"Vehicle ID: {vehicle[0]}, License Plate: {vehicle[1]}, State: {vehicle[2]}, Color: {vehicle[3]}, Make: {vehicle[4]}, Model: {vehicle[5]}, Parking Lot ID: {vehicle[6]}")
        else:
            print("No vehicles found matching the criteria.")
    except Exception as e:
        print(f"An error occurred while performing the set membership filter: {e}")


def set_comparison_similar_cars(db):
    try:
        print("Set Comparison - Similar Cars")
        parking_lot_id = input("Enter the parking lot ID to find similar cars: ").strip()
        query = (
            "SELECT * FROM vehicles "
            "WHERE make IN (SELECT make FROM vehicles WHERE parking_lot_id = ?) "
            "OR model IN (SELECT model FROM vehicles WHERE parking_lot_id = ?) "
            "OR color IN (SELECT color FROM vehicles WHERE parking_lot_id = ?)"
        )
        results = db.cursor.execute(query, (parking_lot_id, parking_lot_id, parking_lot_id)).fetchall()

        if results:
            for vehicle in results:
                print(f"Vehicle ID: {vehicle[0]}, License Plate: {vehicle[1]}, State: {vehicle[2]}, Color: {vehicle[3]}, Make: {vehicle[4]}, Model: {vehicle[5]}, Parking Lot ID: {vehicle[6]}")
        else:
            print("No similar cars found.")
    except Exception as e:
        print(f"An error occurred while performing the set comparison: {e}")


def set_with_subqueries_common_attributes(db):
    try:
        print("Set With Subqueries - Most Common Attributes")
        attribute = input("Enter the attribute to find the most common value for (e.g., color, make, model): ").strip().lower()
        if attribute not in ["color", "make", "model"]:
            print("Invalid attribute. Please select a valid attribute (color, make, model).")
            return

        query = (
            "WITH countTable AS ("
            "    SELECT {}, COUNT({}) AS val_count "
            "    FROM vehicles "
            "    GROUP BY {}"
            ") "
            "SELECT {} FROM countTable WHERE val_count = ("
            "    SELECT MAX(val_count) FROM countTable"
            ")"
        ).format(attribute, attribute, attribute, attribute)
        results = db.cursor.execute(query).fetchall()

        if results:
            print(f"Most common {attribute}: {results[0][0]}")
        else:
            print("No data found.")
    except Exception as e:
        print(f"An error occurred while performing the subquery operation: {e}")


def rank_parking_lots_by_cars(db):
    try:
        print("Rank Parking Lots by Number of Cars")
        query = (
            "WITH countTable AS ("
            "    SELECT parking_lot_id, COUNT(parking_lot_id) AS val_count "
            "    FROM vehicles "
            "    GROUP BY parking_lot_id"
            ") "
            "SELECT DENSE_RANK() OVER (ORDER BY val_count DESC) AS rank, name, val_count "
            "FROM countTable "
            "INNER JOIN parking_lots ON countTable.parking_lot_id = parking_lots.parking_lot_id"
        )
        results = db.cursor.execute(query).fetchall()

        if results:
            for row in results:
                print(f"Rank: {row[0]}, Parking Lot Name: {row[1]}, Number of Cars: {row[2]}")
        else:
            print("No parking lots found.")
    except Exception as e:
        print(f"An error occurred while ranking the parking lots: {e}")


def calculate_available_parking(db):
    try:
        parking_lot_id = input("Enter parking lot ID: ").strip()
        # Get the total capacity of the parking lot
        capacity_query = "SELECT capacity FROM parking_lots WHERE parking_lot_id = ?"
        capacity = db.cursor.execute(capacity_query, (parking_lot_id,)).fetchone()

        if not capacity:
            print("Parking lot not found.")
            return

        # Count the number of vehicles currently in the parking lot
        vehicles_query = "SELECT COUNT(*) FROM vehicles WHERE parking_lot_id = ?"
        vehicles_count = db.cursor.execute(vehicles_query, (parking_lot_id,)).fetchone()[0]

        available_spaces = capacity[0] - vehicles_count
        print(f"Available spaces in parking lot {parking_lot_id}: {available_spaces}")
    except Exception as e:
        print(f"An error occurred while calculating available parking spaces: {e}")


def main():
    db = DBSetup("resources/parking_management.db")

    while True:
        option = main_menu()
        if option == "1":
            while True:
                parking_option = parking_lot_menu()
                if parking_option == "1":
                    add_parking_lot(db)
                elif parking_option == "2":
                    print("Viewing parking lots...")
                    results = db.cursor.execute("SELECT * FROM parking_lots").fetchall()
                    if results:
                        for lot in results:
                            print(f"Parking Lot ID: {lot[0]}, Name: {lot[1]}, Street: {lot[2]}, City: {lot[3]}, State: {lot[4]}, Zip Code: {lot[5]}, Capacity: {lot[6]}")
                    else:
                        print("No parking lots found.")
                elif parking_option == "3":
                    update_parking_lot(db)
                elif parking_option == "4":
                    delete_parking_lot(db)
                elif parking_option == "5":
                    break
        elif option == "2":
            while True:
                vehicle_option = vehicle_menu()
                if vehicle_option == "1":
                    add_vehicle(db)
                elif vehicle_option == "2":
                    print("Viewing vehicles...")
                    results = db.cursor.execute("SELECT * FROM vehicles").fetchall()
                    if results:
                        for vehicle in results:
                            print(f"Vehicle ID: {vehicle[0]}, License Plate: {vehicle[1]}, State: {vehicle[2]}, Color: {vehicle[3]}, Make: {vehicle[4]}, Model: {vehicle[5]}, Parking Lot ID: {vehicle[6]}")
                    else:
                        print("No vehicles found.")
                elif vehicle_option == "3":
                    update_vehicle(db)
                elif vehicle_option == "4":
                    delete_vehicle(db)
                elif vehicle_option == "5":
                    search_vehicle(db)
                elif vehicle_option == "6":
                    set_operations_union(db)
                elif vehicle_option == "7":
                    set_membership_filter(db)
                elif vehicle_option == "8":
                    set_comparison_similar_cars(db)
                elif vehicle_option == "9":
                    set_with_subqueries_common_attributes(db)
                elif vehicle_option == "10":
                    break
        elif option == "3":
            calculate_available_parking(db)
        elif option == "4":
            rank_parking_lots_by_cars(db)
        elif option == "5":
            print("Viewing stats on the number of each car make in individual and total parking lots...")
            # Modified version without using ROLLUP
            query = (
                "SELECT parking_lot_id, make, COUNT(make) "
                "FROM vehicles "
                "GROUP BY parking_lot_id, make "
                "ORDER BY parking_lot_id ASC, make ASC"
            )
            results = db.cursor.execute(query).fetchall()
            if results:
                for row in results:
                    print(f"Parking Lot: {row[0]}, Make: {row[1]}, Count: {row[2]}")
                # Calculate total count for each make
                query_total = (
                    "SELECT make, COUNT(make) "
                    "FROM vehicles "
                    "GROUP BY make "
                    "ORDER BY make ASC"
                )
                total_results = db.cursor.execute(query_total).fetchall()
                print("\nTotal counts for each make:")
                for row in total_results:
                    print(f"Make: {row[0]}, Total Count: {row[1]}")
            else:
                print("No data found.")
        elif option == "6":
            db.disconnect()
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
