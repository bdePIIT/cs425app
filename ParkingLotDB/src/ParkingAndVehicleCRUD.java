import java.util.Scanner;

public class ParkingAndVehicleCRUD {

    public static void main(String[] args) {
        // Create a Scanner object for reading user input
        Scanner scanner = new Scanner(System.in);

        // Main loop for the entire program, runs until user selects Exit
        while (true) {
            // Display the main menu options
            System.out.println("\n--- Parking Lots and Vehicles CRUD Application ---");
            System.out.println("1. Manage Parking Lots");
            System.out.println("2. Manage Vehicles");
            System.out.println("3. Exit");
            System.out.print("Select an option: ");
            int choice = scanner.nextInt();

            // Handle the user's choice for Parking Lot or Vehicle Management
            switch (choice) {
                case 1 -> parkingLotMenu(scanner); // Call the Parking Lot menu
                case 2 -> vehicleMenu(scanner);    // Call the Vehicle menu
                case 3 -> {
                    // Exit the program
                    System.out.println("Exiting program.");
                    return;
                }
                default -> System.out.println("Invalid choice. Try again."); // Handle invalid input
            }
        }
    }

    // Menu for managing Parking Lots
    private static void parkingLotMenu(Scanner scanner) {
        // Loop for handling parking lot management until the user returns to the main menu
        while (true) {
            // Display the Parking Lot management menu
            System.out.println("\n--- Parking Lot Management ---");
            System.out.println("1. Add Parking Lot");
            System.out.println("2. Read Parking Lots");
            System.out.println("3. Update Parking Lot");
            System.out.println("4. Delete Parking Lot");
            System.out.println("5. Back to Main Menu");
            System.out.print("Select an option: ");
            int choice = scanner.nextInt();

            // Handle the user's choice for different Parking Lot actions
            switch (choice) {
                case 1 -> addParkingLot(scanner);      // Call method to add a parking lot
                case 2 -> readParkingLots();           // Call method to read parking lots
                case 3 -> updateParkingLot(scanner);   // Call method to update a parking lot
                case 4 -> deleteParkingLot(scanner);   // Call method to delete a parking lot
                case 5 -> { return; }                  // Return to the main menu
                default -> System.out.println("Invalid choice. Try again."); // Handle invalid input
            }
        }
    }

    // Menu for managing Vehicles
    private static void vehicleMenu(Scanner scanner) {
        // Loop for handling vehicle management until the user returns to the main menu
        while (true) {
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
                case 1 -> addVehicle(scanner);         // Call method to add a vehicle
                case 2 -> readVehicles();              // Call method to read vehicles
                case 3 -> updateVehicle(scanner);      // Call method to update a vehicle
                case 4 -> deleteVehicle(scanner);      // Call method to delete a vehicle
                case 5 -> { return; }                  // Return to the main menu
                default -> System.out.println("Invalid choice. Try again."); // Handle invalid input
            }
        }
    }

    // Placeholder method to add a Parking Lot and prepare an SQL string for later use
    private static void addParkingLot(Scanner scanner) {
        // Prompt user for details about the parking lot
        System.out.print("Enter parking lot name: ");
        String name = "'" + scanner.next() + "'";  // Add single quotes around the string
        System.out.print("Enter street: ");
        String street = "'" + scanner.next() + "'";  // Add single quotes around the string
        System.out.print("Enter city: ");
        String city = "'" + scanner.next() + "'";  // Add single quotes around the string
        System.out.print("Enter state: ");
        String state = "'" + scanner.next() + "'";  // Add single quotes around the string
        System.out.print("Enter zip code: ");
        String zip = "'" + scanner.next() + "'";  // Add single quotes around the string
        System.out.print("Enter capacity: ");
        int capacity = scanner.nextInt();
        
        // Form the string that could be inserted into the database later
        String insertQuery = "INSERT INTO parking_lots (name, street, city, state, zip_code, capacity) VALUES (" 
                            + name + ", " + street + ", " + city + ", " + state + ", " + zip + ", " + capacity + ");";
        
        // Store or print the SQL-like string literal for later use
        System.out.println("Prepared SQL Query for Insertion: " + insertQuery);
        
        // You can later execute this query using a database connection
    }

    // Placeholder method to read Parking Lots (Just prints a placeholder message for now)
    private static void readParkingLots() {
        System.out.println("Read Parking Lots: [This is a test placeholder]");
    }

    // Placeholder method to update a Parking Lot (Currently just displays user input)
    private static void updateParkingLot(Scanner scanner) {
        // Prompt user for details about the parking lot to update
        System.out.print("Enter parking lot ID to update: ");
        int id = scanner.nextInt();
        System.out.print("Enter new name: ");
        String name = "'" + scanner.next() + "'";  // Add single quotes around the string
        System.out.print("Enter new street: ");
        String street = "'" + scanner.next() + "'";  // Add single quotes around the string
        System.out.print("Enter new city: ");
        String city = "'" + scanner.next() + "'";  // Add single quotes around the string
        System.out.print("Enter new state: ");
        String state = "'" + scanner.next() + "'";  // Add single quotes around the string
        System.out.print("Enter new zip code: ");
        String zip = "'" + scanner.next() + "'";  // Add single quotes around the string
        System.out.print("Enter new capacity: ");
        int capacity = scanner.nextInt();
        
        // Form the SQL update query string
        String updateQuery = "UPDATE parking_lots SET name = " + name + ", street = " + street + ", city = " + city + ", state = " + state + ", zip_code = " + zip + ", capacity = " + capacity + " WHERE parking_lot_id = " + id + ";";
        
        // Store or print the SQL-like string literal for later use
        System.out.println("Prepared SQL Query for Update: " + updateQuery);
    }

    // Placeholder method to delete a Parking Lot (Currently just displays the ID entered)
    private static void deleteParkingLot(Scanner scanner) {
        // Prompt user for the parking lot ID to delete
        System.out.print("Enter parking lot ID to delete: ");
        int id = scanner.nextInt();
        System.out.println("Parking lot with ID " + id + " deleted.");
    }

    // Method to add a vehicle and store the result in a string literal for later database insertion
    private static void addVehicle(Scanner scanner) {
        // Prompt user for details about the vehicle
        System.out.print("Enter vehicle license plate: ");
        String licensePlate = "'" + scanner.next() + "'";  // Surround value with single quotes
        System.out.print("Enter state: ");
        String state = "'" + scanner.next() + "'";  // Surround value with single quotes
        System.out.print("Enter color: ");
        String color = "'" + scanner.next() + "'";  // Surround value with single quotes
        System.out.print("Enter make: ");
        String make = "'" + scanner.next() + "'";  // Surround value with single quotes
        System.out.print("Enter model: ");
        String model = "'" + scanner.next() + "'";  // Surround value with single quotes
        
        // Form the string that could be inserted into the database later
        String insertQuery = "INSERT INTO vehicles (license_plate, state, color, make, model) VALUES (" 
                            + licensePlate + ", " + state + ", " + color + ", " + make + ", " + model + ");";
        
        // Store or print the SQL-like string literal for later use
        System.out.println("Prepared SQL Query for Insertion: " + insertQuery);
        
        // You can later execute this query using a database connection
    }

    // Placeholder method to read Vehicles (Just prints a placeholder message for now)
    private static void readVehicles() {
        System.out.println("Read Vehicles: [This is a test placeholder]");
    }

    // Method to update a vehicle and store the update string for later database execution
    private static void updateVehicle(Scanner scanner) {
        // Ask for the vehicle license plate first
        System.out.print("Enter vehicle license plate to update: ");
        String licensePlate = "'" + scanner.next() + "'";  // Surround value with single quotes

        // Display a submenu to choose what fiel2d to update
        System.out.println("What do you want to update?");
        System.out.println("1. State");
        System.out.println("2. Color");
        System.out.println("3. Make");
        System.out.println("4. Model");
        System.out.print("Select an option: ");
        int updateChoice = scanner.nextInt();

        String updateQuery = null;

        // Based on the user's choice, prompt for the new value and create the appropriate SQL update string
        switch (updateChoice) {
            case 1 -> {
                System.out.print("Enter new state: ");
                String state = "'" + scanner.next() + "'";  // Surround value with single quotes
                updateQuery = "UPDATE vehicles SET state = " + state + " WHERE license_plate = " + licensePlate + ";";
            }
            case 2 -> {
                System.out.print("Enter new color: ");
                String color = "'" + scanner.next() + "'";  // Surround value with single quotes
                updateQuery = "UPDATE vehicles SET color = " + color + " WHERE license_plate = " + licensePlate + ";";
            }
            case 3 -> {
                System.out.print("Enter new make: ");
                String make = "'" + scanner.next() + "'";  // Surround value with single quotes
                updateQuery = "UPDATE vehicles SET make = " + make + " WHERE license_plate = " + licensePlate + ";";
            }
            case 4 -> {
                System.out.print("Enter new model: ");
                String model = "'" + scanner.next() + "'";  // Surround value with single quotes
                updateQuery = "UPDATE vehicles SET model = " + model + " WHERE license_plate = " + licensePlate + ";";
            }
            default -> System.out.println("Invalid choice. No updates made.");
        }

        // If a valid update operation was chosen, store or print the SQL-like string literal for later use
        if (updateQuery != null) {
            System.out.println("Prepared SQL Query for Update: " + updateQuery);
        }
    }

    // Placeholder method to delete a Vehicle (Currently just displays the license plate entered)
    private static void deleteVehicle(Scanner scanner) {
        // Prompt user for the vehicle license plate to delete
        System.out.print("Enter vehicle license plate to delete: ");
        String licensePlate = "'" + scanner.next() + "'";  // Surround value with single quotes
        System.out.println("Vehicle with license plate " + licensePlate + " deleted.");
    }
}
