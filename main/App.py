import FreeSimpleGUI as sg
from DBSetup import DBSetup


# Main Menu UI
def main_menu():
    layout = [
        [sg.Text("🚗 Parking Lots and Vehicles Management", font=("Helvetica", 16), justification="center")],
        [sg.HorizontalSeparator()],
        [sg.Button("Manage Parking Lots", size=(30, 1), key="1")],
        [sg.Button("Manage Vehicles", size=(30, 1), key="2")],
        [sg.Button("Calculate Available Spaces", size=(30, 1), key="3")],
        [sg.Button("Rank Parking Lots by Cars", size=(30, 1), key="4")],
        [sg.Button("OLAP - Stats on Car Makes", size=(30, 1), key="5")],
        [sg.Button("Exit", size=(30, 1), key="6")],
    ]
    window = sg.Window("Main Menu", layout, element_justification="center", finalize=True)

    while True:
        event, _ = window.read()
        if event in ("1", "2", "3", "4", "5", "6"):  # Valid options
            window.close()
            return event
        elif event == sg.WINDOW_CLOSED:
            window.close()
            return "6"  # Treat as Exit


# Parking Lot Menu UI
def parking_lot_menu():
    layout = [
        [sg.Text("🅿️ Parking Lot Management", font=("Helvetica", 16), justification="center")],
        [sg.HorizontalSeparator()],
        [sg.Button("Add Parking Lot", size=(30, 1), key="1")],
        [sg.Button("View Parking Lots", size=(30, 1), key="2")],
        [sg.Button("Update Parking Lot", size=(30, 1), key="3")],
        [sg.Button("Delete Parking Lot", size=(30, 1), key="4")],
        [sg.Button("Back to Main Menu", size=(30, 1), key="5")],
    ]
    window = sg.Window("Parking Lot Management", layout, element_justification="center", finalize=True)

    while True:
        event, _ = window.read()
        if event in ("1", "2", "3", "4", "5"):  # Valid options
            window.close()
            return event
        elif event == sg.WINDOW_CLOSED:
            window.close()
            return "5"  # Treat as Back to Main Menu
        
def vehicle_menu():
    # Define the layout for the vehicle menu
    layout = [
        [sg.Text("🚙 Vehicle Management", font=("Helvetica", 16), justification="center")],
        [sg.HorizontalSeparator()],
        [sg.Button("Add Vehicle", size=(40, 1), key="1")],
        [sg.Button("View Vehicles", size=(40, 1), key="2")],
        [sg.Button("Update Vehicle", size=(40, 1), key="3")],
        [sg.Button("Delete Vehicle", size=(40, 1), key="4")],
        [sg.Button("Search Vehicles by Attribute", size=(40, 1), key="5")],
        [sg.Button("Set Operations - Union", size=(40, 1), key="6")],
        [sg.Button("Set Membership - Filter", size=(40, 1), key="7")],
        [sg.Button("Set Comparison - Similar Cars", size=(40, 1), key="8")],
        [sg.Button("Set With Subqueries - Common Attributes", size=(40, 1), key="9")],
        [sg.Button("Back to Main Menu", size=(40, 1), key="10")],
    ]

    # Create the window
    window = sg.Window("Vehicle Management", layout, element_justification="center", finalize=True)

    # Event loop for the window
    while True:
        event, _ = window.read()

        if event in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):  # Valid options
            window.close()
            return event
        elif event == sg.WINDOW_CLOSED:  # User closes the window
            window.close()
            return "10"  # Treat it as going back to the main menu
        
def add_parking_lot(db):
    # Define the layout for the Add Parking Lot form
    layout = [
        [sg.Text("Add Parking Lot", font=("Helvetica", 16), justification="center")],
        [sg.Text("Parking Lot Name", size=(15, 1)), sg.InputText(key="name")],
        [sg.Text("Street", size=(15, 1)), sg.InputText(key="street")],
        [sg.Text("City", size=(15, 1)), sg.InputText(key="city")],
        [sg.Text("State", size=(15, 1)), sg.InputText(key="state")],
        [sg.Text("Zip Code", size=(15, 1)), sg.InputText(key="zip_code")],
        [sg.Text("Capacity", size=(15, 1)), sg.InputText(key="capacity")],
        [sg.Button("Add", size=(10, 1)), sg.Button("Cancel", size=(10, 1))]
    ]

    # Create the window
    window = sg.Window("Add Parking Lot", layout, finalize=True)

    while True:
        event, values = window.read()

        if event == "Add":
            try:
                # Retrieve inputs
                name = values["name"].strip()
                street = values["street"].strip()
                city = values["city"].strip()
                state = values["state"].strip()
                zip_code = values["zip_code"].strip()
                capacity = int(values["capacity"].strip())

                # Insert into the database
                db.cursor.execute(
                    "INSERT INTO parking_lots (name, street, city, state, zip_code, capacity) VALUES (?, ?, ?, ?, ?, ?)",
                    (name, street, city, state, zip_code, capacity)
                )
                db.connection.commit()
                sg.popup("Parking lot added successfully.", title="Success")
                window.close()
                break
            except ValueError:
                sg.popup_error("Please enter valid data. Capacity must be a number.", title="Error")
            except Exception as e:
                sg.popup_error(f"An error occurred: {e}", title="Error")
        elif event in ("Cancel", sg.WINDOW_CLOSED):
            window.close()
            break

def view_parking_lots(db):
    try:
        # Fetch all parking lots
        results = db.cursor.execute("SELECT * FROM parking_lots").fetchall()

        if results:
            # Extract column headers and table data
            headers = ["Parking Lot ID", "Name", "Street", "City", "State", "Zip Code", "Capacity"]
            data = [[lot[0], lot[1], lot[2], lot[3], lot[4], lot[5], lot[6]] for lot in results]

            layout = [
                [sg.Text("Viewing Parking Lots", font=("Helvetica", 16), justification="center")],
                [sg.Table(values=data, headings=headers, auto_size_columns=True, justification="center",
                          num_rows=min(len(data), 20), key="table", enable_events=True)],
                [sg.Button("Close", size=(10, 1))]
            ]

            window = sg.Window("Parking Lots Table", layout, finalize=True)

            while True:
                event, _ = window.read()
                if event in ("Close", sg.WINDOW_CLOSED):
                    window.close()
                    break
        else:
            sg.popup("No parking lots found.", title="No Results")
    except Exception as e:
        sg.popup_error(f"An error occurred: {e}", title="Error")


def add_vehicle(db):
    layout = [
        [sg.Text("Add Vehicle", font=("Helvetica", 16), justification="center")],
        [sg.Text("License Plate", size=(20, 1)), sg.InputText(key="license_plate")],
        [sg.Text("State", size=(20, 1)), sg.InputText(key="state")],
        [sg.Text("Color", size=(20, 1)), sg.InputText(key="color")],
        [sg.Text("Make", size=(20, 1)), sg.InputText(key="make")],
        [sg.Text("Model", size=(20, 1)), sg.InputText(key="model")],
        [sg.Text("Parking Lot ID (Optional)", size=(20, 1)), sg.InputText(key="parking_lot_id")],
        [sg.Button("Add", size=(10, 1)), sg.Button("Cancel", size=(10, 1))]
    ]

    window = sg.Window("Add Vehicle", layout, finalize=True)

    while True:
        event, values = window.read()

        if event == "Add":
            try:
                license_plate = values["license_plate"].strip()
                state = values["state"].strip()
                color = values["color"].strip()
                make = values["make"].strip()
                model = values["model"].strip()
                parking_lot_id = values["parking_lot_id"].strip()
                parking_lot_id = int(parking_lot_id) if parking_lot_id else None

                db.cursor.execute(
                    "INSERT INTO vehicles (license_plate, state, color, make, model, parking_lot_id) VALUES (?, ?, ?, ?, ?, ?)",
                    (license_plate, state, color, make, model, parking_lot_id)
                )
                db.connection.commit()
                sg.popup("Vehicle added successfully.", title="Success")
                window.close()
                break
            except ValueError:
                sg.popup_error("Invalid data provided. Ensure all fields are correct.", title="Error")
            except Exception as e:
                sg.popup_error(f"An error occurred: {e}", title="Error")
        elif event in ("Cancel", sg.WINDOW_CLOSED):
            window.close()
            break

def view_vehicles(db):
    try:
        # Fetch all vehicles
        results = db.cursor.execute("SELECT * FROM vehicles").fetchall()

        if results:
            # Extract column headers and table data
            headers = ["Vehicle ID", "License Plate", "State", "Color", "Make", "Model", "Parking Lot ID"]
            data = [[vehicle[0], vehicle[1], vehicle[2], vehicle[3], vehicle[4], vehicle[5], vehicle[6]] for vehicle in results]

            layout = [
                [sg.Text("Viewing Vehicles", font=("Helvetica", 16), justification="center")],
                [sg.Table(values=data, headings=headers, auto_size_columns=True, justification="center",
                          num_rows=min(len(data), 20), key="table", enable_events=True)],
                [sg.Button("Close", size=(10, 1))]
            ]

            window = sg.Window("Vehicles Table", layout, finalize=True)

            while True:
                event, _ = window.read()
                if event in ("Close", sg.WINDOW_CLOSED):
                    window.close()
                    break
        else:
            sg.popup("No vehicles found.", title="No Results")
    except Exception as e:
        sg.popup_error(f"An error occurred: {e}", title="Error")


def update_parking_lot(db):
    layout = [
        [sg.Text("Update Parking Lot", font=("Helvetica", 16), justification="center")],
        [sg.Text("Parking Lot ID", size=(20, 1)), sg.InputText(key="parking_lot_id")],
        [sg.Text("Select Field to Update:", font=("Helvetica", 12))],
        [sg.Combo(["Name", "Street", "City", "State", "Zip Code", "Capacity"], key="field", size=(20, 1))],
        [sg.Text("New Value", size=(20, 1)), sg.InputText(key="new_value")],
        [sg.Button("Update", size=(10, 1)), sg.Button("Cancel", size=(10, 1))]
    ]

    window = sg.Window("Update Parking Lot", layout, finalize=True)

    while True:
        event, values = window.read()

        if event == "Update":
            try:
                parking_lot_id = values["parking_lot_id"].strip()
                field = values["field"]
                new_value = values["new_value"].strip()

                if not parking_lot_id or not field or not new_value:
                    raise ValueError("All fields must be filled.")

                if field == "Capacity":
                    new_value = int(new_value)  # Ensure capacity is an integer

                db.cursor.execute(
                    f"UPDATE parking_lots SET {field.lower()} = ? WHERE parking_lot_id = ?",
                    (new_value, parking_lot_id)
                )
                db.connection.commit()
                sg.popup("Parking lot updated successfully.", title="Success")
                window.close()
                break
            except ValueError:
                sg.popup_error("Invalid data. Please ensure all fields are filled correctly.", title="Error")
            except Exception as e:
                sg.popup_error(f"An error occurred: {e}", title="Error")
        elif event in ("Cancel", sg.WINDOW_CLOSED):
            window.close()
            break

def delete_parking_lot(db):
    layout = [
        [sg.Text("Delete Parking Lot", font=("Helvetica", 16), justification="center")],
        [sg.Text("Parking Lot ID", size=(20, 1)), sg.InputText(key="parking_lot_id")],
        [sg.Button("Delete", size=(10, 1)), sg.Button("Cancel", size=(10, 1))]
    ]

    window = sg.Window("Delete Parking Lot", layout, finalize=True)

    while True:
        event, values = window.read()

        if event == "Delete":
            try:
                parking_lot_id = values["parking_lot_id"].strip()
                if not parking_lot_id:
                    raise ValueError("Parking Lot ID cannot be empty.")

                db.cursor.execute("DELETE FROM parking_lots WHERE parking_lot_id = ?", (parking_lot_id,))
                db.connection.commit()
                sg.popup("Parking lot deleted successfully.", title="Success")
                window.close()
                break
            except Exception as e:
                sg.popup_error(f"An error occurred: {e}", title="Error")
        elif event in ("Cancel", sg.WINDOW_CLOSED):
            window.close()
            break

def update_vehicle(db):
    layout = [
        [sg.Text("Update Vehicle", font=("Helvetica", 16), justification="center")],
        [sg.Text("Vehicle ID", size=(20, 1)), sg.InputText(key="vehicle_id")],
        [sg.Text("Select Field to Update:", font=("Helvetica", 12))],
        [sg.Combo(["License Plate", "State", "Color", "Make", "Model", "Parking Lot ID"], key="field", size=(20, 1))],
        [sg.Text("New Value", size=(20, 1)), sg.InputText(key="new_value")],
        [sg.Button("Update", size=(10, 1)), sg.Button("Cancel", size=(10, 1))]
    ]

    window = sg.Window("Update Vehicle", layout, finalize=True)

    while True:
        event, values = window.read()

        if event == "Update":
            try:
                vehicle_id = values["vehicle_id"].strip()
                field = values["field"]
                new_value = values["new_value"].strip()

                if not vehicle_id or not field or not new_value:
                    raise ValueError("All fields must be filled.")

                if field == "Parking Lot ID":
                    new_value = int(new_value) if new_value else None

                db.cursor.execute(
                    f"UPDATE vehicles SET {field.replace(' ', '_').lower()} = ? WHERE vehicle_id = ?",
                    (new_value, vehicle_id)
                )
                db.connection.commit()
                sg.popup("Vehicle updated successfully.", title="Success")
                window.close()
                break
            except ValueError:
                sg.popup_error("Invalid data. Please ensure all fields are filled correctly.", title="Error")
            except Exception as e:
                sg.popup_error(f"An error occurred: {e}", title="Error")
        elif event in ("Cancel", sg.WINDOW_CLOSED):
            window.close()
            break

def delete_vehicle(db):
    layout = [
        [sg.Text("Delete Vehicle", font=("Helvetica", 16), justification="center")],
        [sg.Text("Vehicle ID", size=(20, 1)), sg.InputText(key="vehicle_id")],
        [sg.Button("Delete", size=(10, 1)), sg.Button("Cancel", size=(10, 1))]
    ]

    window = sg.Window("Delete Vehicle", layout, finalize=True)

    while True:
        event, values = window.read()

        if event == "Delete":
            try:
                vehicle_id = values["vehicle_id"].strip()
                if not vehicle_id:
                    raise ValueError("Vehicle ID cannot be empty.")

                db.cursor.execute("DELETE FROM vehicles WHERE vehicle_id = ?", (vehicle_id,))
                db.connection.commit()
                sg.popup("Vehicle deleted successfully.", title="Success")
                window.close()
                break
            except Exception as e:
                sg.popup_error(f"An error occurred: {e}", title="Error")
        elif event in ("Cancel", sg.WINDOW_CLOSED):
            window.close()
            break

def search_vehicle(db):
    layout = [
        [sg.Text("Search Vehicles by Attribute", font=("Helvetica", 16), justification="center")],
        [sg.Text("Attribute", size=(20, 1)), sg.Combo(["License Plate", "Color", "Make", "Model"], key="attribute", size=(20, 1))],
        [sg.Text("Search Value", size=(20, 1)), sg.InputText(key="value")],
        [sg.Button("Search", size=(10, 1)), sg.Button("Cancel", size=(10, 1))]
    ]

    window = sg.Window("Search Vehicle", layout, finalize=True)

    while True:
        event, values = window.read()

        if event == "Search":
            try:
                attribute = values["attribute"].lower().replace(" ", "_")
                value = values["value"].strip().lower()

                if not attribute or not value:
                    raise ValueError("Both attribute and search value must be provided.")

                query = f"SELECT * FROM vehicles WHERE LOWER({attribute}) = ?"
                results = db.cursor.execute(query, (value,)).fetchall()

                if results:
                    headers = ["Vehicle ID", "License Plate", "State", "Color", "Make", "Model", "Parking Lot ID"]
                    data = [[vehicle[0], vehicle[1], vehicle[2], vehicle[3], vehicle[4], vehicle[5], vehicle[6]] for vehicle in results]

                    # Display results in a new table window
                    table_layout = [
                        [sg.Text(f"Search Results for {values['attribute']}: {values['value']}", font=("Helvetica", 16), justification="center")],
                        [sg.Table(values=data, headings=headers, auto_size_columns=True, justification="center",
                                  num_rows=min(len(data), 20), key="table", enable_events=True)],
                        [sg.Button("Close", size=(10, 1))]
                    ]

                    table_window = sg.Window("Search Results", table_layout, finalize=True)

                    while True:
                        table_event, _ = table_window.read()
                        if table_event in ("Close", sg.WINDOW_CLOSED):
                            table_window.close()
                            break
                else:
                    sg.popup("No vehicles found matching the criteria.", title="No Results")
            except ValueError as e:
                sg.popup_error(str(e), title="Input Error")
            except Exception as e:
                sg.popup_error(f"An error occurred: {e}", title="Error")
        elif event in ("Cancel", sg.WINDOW_CLOSED):
            window.close()
            break

def set_operations_union(db):
    layout = [
        [sg.Text("Set Operations - Union", font=("Helvetica", 16), justification="center")],
        [sg.Text("First Parking Lot", font=("Helvetica", 12))],
        [sg.Text("Parking Lot ID", size=(20, 1)), sg.InputText(key="parking_lot_id_1")],
        [sg.Text("Attribute", size=(20, 1)), sg.Combo(["Color", "Make", "Model"], key="attribute_1", size=(20, 1))],
        [sg.Text("Value", size=(20, 1)), sg.InputText(key="value_1")],
        [sg.HorizontalSeparator()],
        [sg.Text("Second Parking Lot", font=("Helvetica", 12))],
        [sg.Text("Parking Lot ID", size=(20, 1)), sg.InputText(key="parking_lot_id_2")],
        [sg.Text("Attribute", size=(20, 1)), sg.Combo(["Color", "Make", "Model"], key="attribute_2", size=(20, 1))],
        [sg.Text("Value", size=(20, 1)), sg.InputText(key="value_2")],
        [sg.Button("Execute", size=(10, 1)), sg.Button("Cancel", size=(10, 1))]
    ]

    window = sg.Window("Set Operations - Union", layout, finalize=True)

    while True:
        event, values = window.read()

        if event == "Execute":
            try:
                # Gather inputs
                parking_lot_id_1 = values["parking_lot_id_1"].strip()
                attribute_1 = values["attribute_1"].strip().lower()
                value_1 = values["value_1"].strip().lower()

                parking_lot_id_2 = values["parking_lot_id_2"].strip()
                attribute_2 = values["attribute_2"].strip().lower()
                value_2 = values["value_2"].strip().lower()

                valid_attributes = ["color", "make", "model"]

                # Validate inputs
                if not parking_lot_id_1 or not parking_lot_id_2 or not attribute_1 or not attribute_2 or not value_1 or not value_2:
                    raise ValueError("All fields must be filled.")

                if attribute_1 not in valid_attributes or attribute_2 not in valid_attributes:
                    raise ValueError("Invalid attributes selected. Please choose from Color, Make, or Model.")

                # Execute query
                query = (
                    "SELECT * FROM vehicles WHERE parking_lot_id = ? AND LOWER({}) = ? "
                    "UNION "
                    "SELECT * FROM vehicles WHERE parking_lot_id = ? AND LOWER({}) = ?"
                ).format(attribute_1, attribute_2)

                results = db.cursor.execute(query, (parking_lot_id_1, value_1, parking_lot_id_2, value_2)).fetchall()

                if results:
                    headers = ["Vehicle ID", "License Plate", "State", "Color", "Make", "Model", "Parking Lot ID"]
                    data = [[vehicle[0], vehicle[1], vehicle[2], vehicle[3], vehicle[4], vehicle[5], vehicle[6]] for vehicle in results]

                    # Display results in a table
                    table_layout = [
                        [sg.Text("Union Results", font=("Helvetica", 16), justification="center")],
                        [sg.Table(values=data, headings=headers, auto_size_columns=True, justification="center",
                                  num_rows=min(len(data), 20), key="table", enable_events=True)],
                        [sg.Button("Close", size=(10, 1))]
                    ]

                    table_window = sg.Window("Union Results", table_layout, finalize=True)

                    while True:
                        table_event, _ = table_window.read()
                        if table_event in ("Close", sg.WINDOW_CLOSED):
                            table_window.close()
                            break
                else:
                    sg.popup("No vehicles found matching the criteria.", title="No Results")
            except ValueError as e:
                sg.popup_error(str(e), title="Input Error")
            except Exception as e:
                sg.popup_error(f"An error occurred: {e}", title="Error")
        elif event in ("Cancel", sg.WINDOW_CLOSED):
            window.close()
            break

def set_membership_filter(db):
    layout = [
        [sg.Text("Set Membership - Filter", font=("Helvetica", 16), justification="center")],
        [sg.Text("Attribute", size=(20, 1)), sg.Combo(["Color", "Make", "Model"], key="attribute", size=(20, 1))],
        [sg.Text("Values to Exclude (comma-separated)", size=(30, 1)), sg.InputText(key="values")],
        [sg.Button("Filter", size=(10, 1)), sg.Button("Cancel", size=(10, 1))]
    ]

    window = sg.Window("Set Membership - Filter", layout, finalize=True)

    while True:
        event, values = window.read()

        if event == "Filter":
            try:
                # Gather inputs
                attribute = values["attribute"].strip().lower()
                values_to_exclude = [value.strip().lower() for value in values["values"].split(",")]

                if not attribute or not values_to_exclude:
                    raise ValueError("Both attribute and exclusion values must be provided.")

                valid_attributes = ["color", "make", "model"]
                if attribute not in valid_attributes:
                    raise ValueError("Invalid attribute selected. Please choose from Color, Make, or Model.")

                # Prepare query
                placeholders = ', '.join('?' for _ in values_to_exclude)
                query = f"SELECT * FROM vehicles WHERE LOWER({attribute}) NOT IN ({placeholders})"
                results = db.cursor.execute(query, values_to_exclude).fetchall()

                if results:
                    headers = ["Vehicle ID", "License Plate", "State", "Color", "Make", "Model", "Parking Lot ID"]
                    data = [[vehicle[0], vehicle[1], vehicle[2], vehicle[3], vehicle[4], vehicle[5], vehicle[6]] for vehicle in results]

                    # Display results in a table
                    table_layout = [
                        [sg.Text("Filter Results", font=("Helvetica", 16), justification="center")],
                        [sg.Table(values=data, headings=headers, auto_size_columns=True, justification="center",
                                  num_rows=min(len(data), 20), key="table", enable_events=True)],
                        [sg.Button("Close", size=(10, 1))]
                    ]

                    table_window = sg.Window("Filter Results", table_layout, finalize=True)

                    while True:
                        table_event, _ = table_window.read()
                        if table_event in ("Close", sg.WINDOW_CLOSED):
                            table_window.close()
                            break
                else:
                    sg.popup("No vehicles found matching the criteria.", title="No Results")
            except ValueError as e:
                sg.popup_error(str(e), title="Input Error")
            except Exception as e:
                sg.popup_error(f"An error occurred: {e}", title="Error")
        elif event in ("Cancel", sg.WINDOW_CLOSED):
            window.close()
            break

def set_comparison_similar_cars(db):
    layout = [
        [sg.Text("Set Comparison - Similar Cars", font=("Helvetica", 16), justification="center")],
        [sg.Text("Parking Lot ID", size=(20, 1)), sg.InputText(key="parking_lot_id")],
        [sg.Button("Find Similar Cars", size=(15, 1)), sg.Button("Cancel", size=(10, 1))]
    ]

    window = sg.Window("Set Comparison - Similar Cars", layout, finalize=True)

    while True:
        event, values = window.read()

        if event == "Find Similar Cars":
            try:
                # Gather input
                parking_lot_id = values["parking_lot_id"].strip()
                if not parking_lot_id:
                    raise ValueError("Parking Lot ID must be provided.")

                # Query to find similar cars restricted to the specified parking lot
                query = (
                    "SELECT * FROM vehicles "
                    "WHERE parking_lot_id = ? "
                    "AND (make IN (SELECT make FROM vehicles WHERE parking_lot_id = ?) "
                    "OR model IN (SELECT model FROM vehicles WHERE parking_lot_id = ?) "
                    "OR color IN (SELECT color FROM vehicles WHERE parking_lot_id = ?))"
                )
                results = db.cursor.execute(query, (parking_lot_id, parking_lot_id, parking_lot_id, parking_lot_id)).fetchall()

                if results:
                    headers = ["Vehicle ID", "License Plate", "State", "Color", "Make", "Model", "Parking Lot ID"]
                    data = [[vehicle[0], vehicle[1], vehicle[2], vehicle[3], vehicle[4], vehicle[5], vehicle[6]] for vehicle in results]

                    # Display results in a table
                    table_layout = [
                        [sg.Text("Similar Cars", font=("Helvetica", 16), justification="center")],
                        [sg.Table(values=data, headings=headers, auto_size_columns=True, justification="center",
                                  num_rows=min(len(data), 20), key="table", enable_events=True)],
                        [sg.Button("Close", size=(10, 1))]
                    ]

                    table_window = sg.Window("Similar Cars", table_layout, finalize=True)

                    while True:
                        table_event, _ = table_window.read()
                        if table_event in ("Close", sg.WINDOW_CLOSED):
                            table_window.close()
                            break
                else:
                    sg.popup("No similar cars found.", title="No Results")
            except ValueError as e:
                sg.popup_error(str(e), title="Input Error")
            except Exception as e:
                sg.popup_error(f"An error occurred: {e}", title="Error")
        elif event in ("Cancel", sg.WINDOW_CLOSED):
            window.close()
            break

def set_with_subqueries_common_attributes(db):
    layout = [
        [sg.Text("Set With Subqueries - Most Common Attributes", font=("Helvetica", 16), justification="center")],
        [sg.Text("Attribute", size=(20, 1)), sg.Combo(["Color", "Make", "Model"], key="attribute", size=(20, 1))],
        [sg.Button("Find Most Common", size=(15, 1)), sg.Button("Cancel", size=(10, 1))]
    ]

    window = sg.Window("Most Common Attributes", layout, finalize=True)

    while True:
        event, values = window.read()

        if event == "Find Most Common":
            try:
                attribute = values["attribute"].lower()
                if not attribute:
                    raise ValueError("Attribute must be selected.")

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
                    sg.popup(f"Most common {attribute}: {results[0][0]}", title="Result")
                else:
                    sg.popup("No data found.", title="No Results")
            except Exception as e:
                sg.popup_error(f"An error occurred: {e}", title="Error")
        elif event in ("Cancel", sg.WINDOW_CLOSED):
            window.close()
            break

def calculate_available_parking(db):
    layout = [
        [sg.Text("Calculate Available Parking", font=("Helvetica", 16), justification="center")],
        [sg.Text("Parking Lot ID", size=(20, 1)), sg.InputText(key="parking_lot_id")],
        [sg.Button("Calculate", size=(10, 1)), sg.Button("Cancel", size=(10, 1))]
    ]

    window = sg.Window("Calculate Available Parking", layout, finalize=True)

    while True:
        event, values = window.read()

        if event == "Calculate":
            try:
                parking_lot_id = values["parking_lot_id"].strip()
                if not parking_lot_id:
                    raise ValueError("Parking Lot ID cannot be empty.")

                # Get the total capacity of the parking lot
                capacity_query = "SELECT capacity FROM parking_lots WHERE parking_lot_id = ?"
                capacity = db.cursor.execute(capacity_query, (parking_lot_id,)).fetchone()

                if not capacity:
                    sg.popup("Parking lot not found.", title="Error")
                    continue

                # Count the number of vehicles currently in the parking lot
                vehicles_query = "SELECT COUNT(*) FROM vehicles WHERE parking_lot_id = ?"
                vehicles_count = db.cursor.execute(vehicles_query, (parking_lot_id,)).fetchone()[0]

                available_spaces = capacity[0] - vehicles_count
                sg.popup(f"Available spaces in parking lot {parking_lot_id}: {available_spaces}", title="Result")
            except Exception as e:
                sg.popup_error(f"An error occurred: {e}", title="Error")
        elif event in ("Cancel", sg.WINDOW_CLOSED):
            window.close()
            break

def rank_parking_lots_by_cars(db):
    try:
        # Query to rank parking lots by the number of cars
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
            # Prepare headers and data for the table
            headers = ["Rank", "Parking Lot Name", "Number of Cars"]
            data = [[row[0], row[1], row[2]] for row in results]

            # Define the layout for the UI
            layout = [
                [sg.Text("Ranked Parking Lots by Number of Cars", font=("Helvetica", 16), justification="center")],
                [sg.Table(values=data, headings=headers, auto_size_columns=True, justification="center",
                          num_rows=min(len(data), 20), key="table", enable_events=True)],
                [sg.Button("Close", size=(10, 1))]
            ]

            # Create the window
            window = sg.Window("Parking Lot Rankings", layout, finalize=True)

            # Event loop for the window
            while True:
                event, _ = window.read()
                if event in ("Close", sg.WINDOW_CLOSED):
                    window.close()
                    break
        else:
            sg.popup("No parking lots found.", title="No Results")
    except Exception as e:
        sg.popup_error(f"An error occurred: {e}", title="Error")

def view_car_make_stats(db):
    try:
        # Query for individual parking lot stats
        query = (
            "SELECT parking_lot_id, make, COUNT(make) "
            "FROM vehicles "
            "GROUP BY parking_lot_id, make "
            "ORDER BY parking_lot_id ASC, make ASC"
        )
        results = db.cursor.execute(query).fetchall()

        # Query for total stats across all parking lots
        query_total = (
            "SELECT make, COUNT(make) "
            "FROM vehicles "
            "GROUP BY make "
            "ORDER BY make ASC"
        )
        total_results = db.cursor.execute(query_total).fetchall()

        if results or total_results:
            # Prepare headers and data for individual stats
            headers_individual = ["Parking Lot ID", "Make", "Count"]
            data_individual = [[row[0], row[1], row[2]] for row in results]

            # Prepare headers and data for total stats
            headers_total = ["Make", "Total Count"]
            data_total = [[row[0], row[1]] for row in total_results]

            # Define the layout for the UI
            layout = [
                [sg.Text("Car Make Stats by Parking Lot", font=("Helvetica", 16), justification="center")],
                [sg.Table(values=data_individual, headings=headers_individual, auto_size_columns=True,
                          justification="center", num_rows=min(len(data_individual), 20), key="table1")],
                [sg.Text("Total Car Make Stats Across All Lots", font=("Helvetica", 16), justification="center")],
                [sg.Table(values=data_total, headings=headers_total, auto_size_columns=True,
                          justification="center", num_rows=min(len(data_total), 20), key="table2")],
                [sg.Button("Close", size=(10, 1))]
            ]

            # Create the window
            window = sg.Window("Car Make Stats", layout, finalize=True)

            # Event loop for the window
            while True:
                event, _ = window.read()
                if event in ("Close", sg.WINDOW_CLOSED):
                    window.close()
                    break
        else:
            sg.popup("No data found.", title="No Results")
    except Exception as e:
        sg.popup_error(f"An error occurred: {e}", title="Error")

# Main Program Logic
def main():
    db = DBSetup("resources/parking_management.db")

    while True:
        option = main_menu()  # GUI-based main menu
        if option == "1":
            while True:
                parking_option = parking_lot_menu()  # GUI-based parking lot menu
                if parking_option == "1":
                    add_parking_lot(db)
                elif parking_option == "2":
                    view_parking_lots(db)
                elif parking_option == "3":
                    update_parking_lot(db)
                elif parking_option == "4":
                    delete_parking_lot(db)
                elif parking_option == "5":
                    break
        elif option == "2":
            while True:
                vehicle_option = vehicle_menu()  # Replace with GUI-based vehicle menu
                if vehicle_option == "1":
                    add_vehicle(db)
                elif vehicle_option == "2":
                    view_vehicles(db)
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
            view_car_make_stats(db)
        elif option == "6":
            db.disconnect()
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
