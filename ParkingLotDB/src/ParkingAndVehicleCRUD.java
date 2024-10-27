import java.util.Scanner;
import java.util.ArrayList;

public class ParkingAndVehicleCRUD {

    public static DBInterface db = new DBInterface();

    public static void main(String[] args) {
        db.connect();
        // Create a Scanner object for reading user input
        Scanner scanner = new Scanner(System.in);

        // Main loop for the entire program, runs until user selects Exit
        while (true) {
            try {
                // Display the main menu options
                System.out.println("\n--- Parking Lots and Vehicles CRUD Application ---");
                System.out.println("1. Manage Parking Lots");
                System.out.println("2. Manage Vehicles");
                System.out.println("3. Exit");
                System.out.print("Select an option: ");

                int choice = scanner.nextInt(); // read user input

                // Handle the user's choice for Parking Lot or Vehicle Management
                switch (choice) {
                    case 1 -> parkingLotMenu(scanner); // Call the Parking Lot menu
                    case 2 -> vehicleMenu(scanner); // Call the Vehicle menu
                    case 3 -> {
                        // Exit the program
                        System.out.println("Closing app.");
                        db.disconnect();
                        return;
                    }
                    default -> throw new Exception(); // Handle invalid input
                }
            } catch (Exception e) {
                System.out.println("\nInvalid input. Please enter a valid number.");
                scanner.nextLine(); // Clear the invalid input
            }
        }
    }

    // Menu for managing Parking Lots
    private static void parkingLotMenu(Scanner scanner) {
        // Loop for handling parking lot management until the user returns to the main
        // menu
        while (true) {
            try {
                // Display the Parking Lot management menu
                System.out.println("\n--- Parking Lot Management ---");
                System.out.println("1. Add Parking Lot");
                System.out.println("2. Read Parking Lots");
                System.out.println("3. Update Parking Lot");
                System.out.println("4. Delete Parking Lot");
                System.out.println("5. Back to Main Menu");
                System.out.print("Select an option: ");

                int choice = scanner.nextInt(); // read user input

                // Handle the user's choice for different Parking Lot actions
                switch (choice) {
                    case 1 -> addParkingLot(scanner); // Call method to add a parking lot
                    case 2 -> readParkingLots(); // Call method to read parking lots
                    case 3 -> updateParkingLot(scanner); // Call method to update a parking lot
                    case 4 -> deleteParkingLot(scanner); // Call method to delete a parking lot
                    case 5 -> {
                        return;
                    } // Return to the main menu
                    default -> throw new Exception(); // Handle invalid input
                }
            } catch (Exception e) {
                System.out.println("\nInvalid input. Please enter a valid number.");
                scanner.nextLine(); // Clear the invalid input
            }
        }
    }

    // Menu for managing Vehicles
    private static void vehicleMenu(Scanner scanner) {
        // Loop for handling vehicle management until the user returns to the main menu
        while (true) {
            try {
                // Display the Vehicle management menu
                System.out.println("\n--- Vehicle Management ---");
                System.out.println("1. Add Vehicle");
                System.out.println("2. Read Vehicles");
                System.out.println("3. Update Vehicle");
                System.out.println("4. Delete Vehicle");
                System.out.println("5. Back to Main Menu");
                System.out.print("Select an option: ");
                int choice = scanner.nextInt();

                // Handle the user's choice for different Vehicle actions
                switch (choice) {
                    case 1 -> addVehicle(scanner); // Call method to add a vehicle
                    case 2 -> readVehicles(); // Call method to read vehicles
                    case 3 -> updateVehicle(scanner); // Call method to update a vehicle
                    case 4 -> deleteVehicle(scanner); // Call method to delete a vehicle
                    case 5 -> {
                        return;
                    } // Return to the main menu
                    default -> throw new Exception(); // Handle invalid input
                }
            } catch (Exception e) {
                System.out.println("\nInvalid input. Please enter a valid number.");
                scanner.nextLine(); // Clear the invalid input
            }
        }
    }

    // Placeholder method to add a Parking Lot
    private static void addParkingLot(Scanner scanner) {
        try {
            // Prompt user for details about the parking lot
            System.out.print("Enter parking lot name: ");
            String name = "'" + scanner.next() + "'"; // Add single quotes around the string
            System.out.print("Enter street: ");
            String street = "'" + scanner.next() + "'"; // Add single quotes around the string
            System.out.print("Enter city: ");
            String city = "'" + scanner.next() + "'"; // Add single quotes around the string
            System.out.print("Enter state: ");
            String state = "'" + scanner.next() + "'"; // Add single quotes around the string
            System.out.print("Enter zip code: ");
            String zip = "'" + scanner.next() + "'"; // Add single quotes around the string
            System.out.print("Enter capacity: ");
            int capacity = scanner.nextInt();

            db.insert("parking_lots", new String[] { name, street, city, state, zip, "" + capacity });
        } catch (Exception e) {
            System.err.println("Error adding parking lot.");
        }
    }

    // Placeholder method to read Parking Lots (Just prints a placeholder message
    // for now)
    private static void readParkingLots() {
        System.out.println("Parking Lots:");
        System.out.println("[Name, Street, City, State, Zip Code, Capacity]");
        printArrayList(db.readAllRows("parking_lots",
                new String[] { "parking_lot_id", "name", "street", "city", "state", "zip_code", "capacity" }));
    }

    // Placeholder method to update a Parking Lot (Currently just displays user
    // input)
    private static void updateParkingLot(Scanner scanner) {
        // Ask for the parking lot ID first
        System.out.print("Enter parking lot ID to update: ");
        int id = scanner.nextInt();

        if (!parkingLotExists(id + "")) {
            System.out.println("Parking lot doesn't exist!\nReturning.");
            return;
        }

        // Display a submenu to choose which field to update
        System.out.println("What do you want to update?");
        System.out.println("1. Name");
        System.out.println("2. Street");
        System.out.println("3. City");
        System.out.println("4. State");
        System.out.println("5. Zip Code");
        System.out.println("6. Capacity");
        System.out.print("Select an option: ");
        int updateChoice = scanner.nextInt();

        String attr = null;
        String val = null;

        // Based on the user's choice, prompt for the new value and create the formatted
        // update string
        switch (updateChoice) {
            case 1 -> {
                System.out.print("Enter new name: ");
                String name = "'" + scanner.next() + "'";
                // formattedUpdate = "update(\"parking_lots\", \"name\", " + name + ",
                // \"parking_lot_id\", " + id + ")";
                attr = "name";
                val = name;
            }
            case 2 -> {
                System.out.print("Enter new street: ");
                String street = "'" + scanner.next() + "'";
                // formattedUpdate = "update(\"parking_lots\", \"street\", " + street + ",
                // \"parking_lot_id\", " + id + ")";
                attr = "street";
                val = street;
            }
            case 3 -> {
                System.out.print("Enter new city: ");
                String city = "'" + scanner.next() + "'";
                // formattedUpdate = "update(\"parking_lots\", \"city\", " + city + ",
                // \"parking_lot_id\", " + id + ")";
                attr = "city";
                val = city;
            }
            case 4 -> {
                System.out.print("Enter new state: ");
                String state = "'" + scanner.next() + "'";
                // formattedUpdate = "update(\"parking_lots\", \"state\", " + state + ",
                // \"parking_lot_id\", " + id + ")";
                attr = "state";
                val = state;
            }
            case 5 -> {
                System.out.print("Enter new zip code: ");
                String zipCode = "'" + scanner.next() + "'";
                // formattedUpdate = "update(\"parking_lots\", \"zip_code\", " + zipCode + ",
                // \"parking_lot_id\", " + id + ")";
                attr = "zip_code";
                val = zipCode;
            }
            case 6 -> {
                System.out.print("Enter new capacity: ");
                int capacity = scanner.nextInt();
                // formattedUpdate = "update(\"parking_lots\", \"capacity\", " + capacity + ",
                // \"parking_lot_id\", " + id + ")";
                attr = "capacity";
                val = capacity + "";
            }
            default -> System.out.println("Invalid choice. No updates made.");
        }

        // If a valid update operation was chosen, print the formatted update command
        if (attr != null) {
            // System.out.println("Formatted Update Command: " + formattedUpdate);
            db.update("parking_lots", attr, val, "parking_lot_id", id + "");
        }
    }

    // Placeholder method to delete a Parking Lot (Currently just displays the ID
    // entered)
    private static void deleteParkingLot(Scanner scanner) {
        // Prompt user for the parking lot ID to delete
        System.out.print("Enter parking lot ID to delete: ");
        int id = scanner.nextInt();
        System.out.println("Parking lot with ID " + id + " deleted.");
        db.delete("parking_lots", "parking_lot_id", id + "");
    }

    // Method to add a vehicle and store the result in a string literal for later
    // database insertion
    private static void addVehicle(Scanner scanner) {
        // Prompt user for details about the vehicle
        System.out.print("Enter vehicle license plate: ");
        String licensePlate = "'" + scanner.next() + "'"; // Surround value with single quotes
        System.out.print("Enter state: ");
        String state = "'" + scanner.next() + "'"; // Surround value with single quotes
        System.out.print("Enter color: ");
        String color = "'" + scanner.next() + "'"; // Surround value with single quotes
        System.out.print("Enter make: ");
        String make = "'" + scanner.next() + "'"; // Surround value with single quotes
        System.out.print("Enter model: ");
        String model = "'" + scanner.next() + "'"; // Surround value with single quotes
        System.out.print("Enter parking lot id: ");
        String parkingLotID = scanner.next() + "";

        /* Check if Parking Lot with that ID Exist!! */
        if (!parkingLotExists(parkingLotID)) {
            System.out.println("Parking Lot with that ID doesn't exist!\nReturning.");
        }

        // // Form the string that could be inserted into the database later
        // String insertQuery = "INSERT INTO vehicles (license_plate, state, color,
        // make, model) VALUES ("
        // + licensePlate + ", " + state + ", " + color + ", " + make + ", " + model +
        // ");";

        // // Store or print the SQL-like string literal for later use
        // System.out.println("Prepared SQL Query for Insertion: " + insertQuery);

        // You can later execute this query using a database connection
        db.insert("vehicles", new String[] { licensePlate, state, parkingLotID, color, make, model });
    }

    /*
     * Checks if a parking lot with the id ID exists. True if yes, false if not.
     */
    private static boolean parkingLotExists(String id) {
        ArrayList<String[]> res = db.read("parking_lots", new String[] { "parking_lot_id" }, "parking_lot_id", id);
        return !res.isEmpty();
    }

    /*
     * Checks if a vehicle with the license plate exists. True if yes, false if not.
     */
    private static boolean vehicleExists(String licensePlate) {
        ArrayList<String[]> res = db.read("vehicles", new String[] { "license_plate" }, "license_plate", licensePlate);
        return !res.isEmpty();
    }

    // Placeholder method to read Vehicles (Just prints a placeholder message for
    // now)
    private static void readVehicles() {
        // System.out.println("Read Vehicles: [This is a test placeholder]");
        System.out.println("Vehicles:");
        System.out.println("[License Plate, State, Color, Make, Model]");
        printArrayList(db.readAllRows("vehicles",
                new String[] { "license_plate", "state", "parking_lot_id", "color", "make", "model" }));
    }

    // Method to update a vehicle and store the update string for later database
    // execution
    private static void updateVehicle(Scanner scanner) {
        // Ask for the vehicle license plate first
        System.out.print("Enter vehicle license plate to update: ");
        String licensePlate = "'" + scanner.next() + "'"; // Surround value with single quotes

        if (!vehicleExists(licensePlate)) {
            System.out.println("Vehicle doesn't exist!\nReturning.");
            return;
        }

        // Display a submenu to choose what field to update
        System.out.println("What do you want to update?");
        System.out.println("1. State");
        System.out.println("2. Color");
        System.out.println("3. Make");
        System.out.println("4. Model");
        System.out.println("5. Parking Lot ID");
        System.out.print("Select an option: ");
        int updateChoice = scanner.nextInt();

        String attr = null;
        String val = null;

        // Based on the user's choice, prompt for the new value and create the
        // appropriate SQL update string
        switch (updateChoice) {
            case 1 -> {
                System.out.print("Enter new state: ");
                String state = "'" + scanner.next() + "'"; // Surround value with single quotes
                // updateQuery = "UPDATE vehicles SET state = " + state + " WHERE license_plate
                // = " + licensePlate + ";";
                attr = "state";
                val = state;
            }
            case 2 -> {
                System.out.print("Enter new color: ");
                String color = "'" + scanner.next() + "'"; // Surround value with single quotes
                // updateQuery = "UPDATE vehicles SET color = " + color + " WHERE license_plate
                // = " + licensePlate + ";";
                attr = "color";
                val = color;
            }
            case 3 -> {
                System.out.print("Enter new make: ");
                String make = "'" + scanner.next() + "'"; // Surround value with single quotes
                // updateQuery = "UPDATE vehicles SET make = " + make + " WHERE license_plate =
                // " + licensePlate + ";";
                attr = "make";
                val = make;
            }
            case 4 -> {
                System.out.print("Enter new model: ");
                String model = "'" + scanner.next() + "'"; // Surround value with single quotes
                // updateQuery = "UPDATE vehicles SET model = " + model + " WHERE license_plate
                // = " + licensePlate + ";";
                attr = "model";
                val = model;
            }
            case 5 -> {
                System.out.print("Enter new parking lot ID: ");
                String id = scanner.next() + "";
                if (!parkingLotExists(id)) {
                    System.out.println("Invalid parking lot! No updates made.");
                    break;
                }
                attr = "parking_lot_id";
                val = id;
            }
            default -> System.out.println("Invalid choice. No updates made.");
        }

        if (attr != null) {
            db.update("vehicles", attr, val, "license_plate", licensePlate);
        }
    }

    // Placeholder method to delete a Vehicle (Currently just displays the license
    // plate entered)
    private static void deleteVehicle(Scanner scanner) {
        // Prompt user for the vehicle license plate to delete
        System.out.print("Enter vehicle license plate to delete: ");
        String licensePlate = "'" + scanner.next() + "'"; // Surround value with single quotes
        db.delete("vehicles", "license_plate", licensePlate);
        System.out.println("Vehicle with license plate " + licensePlate + " deleted.");
    }

    public static void printArrayList(ArrayList<String[]> list) {
        for (String[] sarr : list) {
            System.out.println("[" + String.join(",", sarr) + "]");
        }
    }
}
