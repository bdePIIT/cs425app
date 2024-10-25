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

    // Method to add a Parking Lot in the specified format
    private static void addParkingLot(Scanner scanner) {
        // Prompt user for details about the parking lot
        System.out.print("Enter parking lot name: ");
        String name = "'" + scanner.next() + "'";
        System.out.print("Enter street: ");
        String street = "'" + scanner.next() + "'";
        System.out.print("Enter city: ");
        String city = "'" + scanner.next() + "'";
        System.out.print("Enter state: ");
        String state = "'" + scanner.next() + "'";
        System.out.print("Enter zip code: ");
        String zipCode = "'" + scanner.next() + "'";
        System.out.print("Enter capacity: ");
        int capacity = scanner.nextInt();
        
        // Store the formatted string for insertion
        String formattedInsert = "insert(\"parking_lots\", [" + name + ", " + street + ", " + city + ", " + state + ", " + zipCode + ", " + capacity + "])";
        
        // Print or store the formatted string for later use
        System.out.println("Formatted Insert Command: " + formattedInsert);
    }

    // Method to update a Parking Lot
    private static void updateParkingLot(Scanner scanner) {
        System.out.print("Enter parking lot ID to update: ");
        int id = scanner.nextInt();

        // Display a submenu to choose what field to update
        System.out.println("What do you want to update?");
        System.out.println("1. Name");
        System.out.println("2. Street");
        System.out.println("3. City");
        System.out.println("4. State");
        System.out.println("5. Zip Code");
        System.out.println("6. Capacity");
        System.out.print("Select an option: ");
        int updateChoice = scanner.nextInt();

        String formattedUpdate = null;

        // Based on the user's choice, prompt for the new value and create the formatted update string
        switch (updateChoice) {
            case 1 -> {
                System.out.print("Enter new name: ");
                String name = "'" + scanner.next() + "'";
                formattedUpdate = "update(\"parking_lots\", \"name\", " + name + ", \"parking_lot_id\", " + id + ")";
            }
            case 2 -> {
                System.out.print("Enter new street: ");
                String street = "'" + scanner.next() + "'";
                formattedUpdate = "update(\"parking_lots\", \"street\", " + street + ", \"parking_lot_id\", " + id + ")";
            }
            case 3 -> {
                System.out.print("Enter new city: ");
                String city = "'" + scanner.next() + "'";
                formattedUpdate = "update(\"parking_lots\", \"city\", " + city + ", \"parking_lot_id\", " + id + ")";
            }
            case 4 -> {
                System.out.print("Enter new state: ");
                String state = "'" + scanner.next() + "'";
                formattedUpdate = "update(\"parking_lots\", \"state\", " + state + ", \"parking_lot_id\", " + id + ")";
            }
            case 5 -> {
                System.out.print("Enter new zip code: ");
                String zipCode = "'" + scanner.next() + "'";
                formattedUpdate = "update(\"parking_lots\", \"zip_code\", " + zipCode + ", \"parking_lot_id\", " + id + ")";
            }
            case 6 -> {
                System.out.print("Enter new capacity: ");
                int capacity = scanner.nextInt();
                formattedUpdate = "update(\"parking_lots\", \"capacity\", " + capacity + ", \"parking_lot_id\", " + id + ")";
            }
            default -> System.out.println("Invalid choice. No updates made.");
        }

        if (formattedUpdate != null) {
            System.out.println("Formatted Update Command: " + formattedUpdate);
        }
    }

    // Method to delete a Parking Lot
    private static void deleteParkingLot(Scanner scanner) {
        System.out.print("Enter parking lot ID to delete: ");
        int id = scanner.nextInt();
        String formattedDelete = "delete(\"parking_lots\", \"parking_lot_id\", " + id + ")";
        System.out.println("Formatted Delete Command: " + formattedDelete);
    }

    // Method to add a vehicle in the specified format
    private static void addVehicle(Scanner scanner) {
        System.out.print("Enter vehicle license plate: ");
        String licensePlate = "'" + scanner.next() + "'";
        System.out.print("Enter state: ");
        String state = "'" + scanner.next() + "'";
        System.out.print("Enter color: ");
        String color = "'" + scanner.next() + "'";
        System.out.print("Enter make: ");
        String make = "'" + scanner.next() + "'";
        System.out.print("Enter model: ");
        String model = "'" + scanner.next() + "'";
        
        String formattedInsert = "insert(\"vehicles\", [" + licensePlate + ", " + state + ", " + color + ", " + make + ", " + model + "])";
        
        System.out.println("Formatted Insert Command: " + formattedInsert);
    }

    // Method to update a vehicle
    private static void updateVehicle(Scanner scanner) {
        System.out.print("Enter vehicle license plate to update: ");
        String licensePlate = "'" + scanner.next() + "'";

        System.out.println("What do you want to update?");
        System.out.println("1. State");
        System.out.println("2. Color");
        System.out.println("3. Make");
        System.out.println("4. Model");
        System.out.print("Select an option: ");
        int updateChoice = scanner.nextInt();

        String formattedUpdate = null;

        switch (updateChoice) {
            case 1 -> {
                System.out.print("Enter new state: ");
                String state = "'" + scanner.next() + "'";
                formattedUpdate = "update(\"vehicles\", \"state\", " + state + ", \"license_plate\", " + licensePlate + ")";
            }
            case 2 -> {
                System.out.print("Enter new color: ");
                String color = "'" + scanner.next() + "'";
                formattedUpdate = "update(\"vehicles\", \"color\", " + color + ", \"license_plate\", " + licensePlate + ")";
            }
            case 3 -> {
                System.out.print("Enter new make: ");
                String make = "'" + scanner.next() + "'";
                formattedUpdate = "update(\"vehicles\", \"make\", " + make + ", \"license_plate\", " + licensePlate + ")";
            }
            case 4 -> {
                System.out.print("Enter new model: ");
                String model = "'" + scanner.next() + "'";
                formattedUpdate = "update(\"vehicles\", \"model\", " + model + ", \"license_plate\", " + licensePlate + ")";
            }
            default -> System.out.println("Invalid choice. No updates made.");
        }

        if (formattedUpdate != null) {
            System.out.println("Formatted Update Command: " + formattedUpdate);
        }
    }

    // Method to delete a Vehicle
    private static void deleteVehicle(Scanner scanner) {
        System.out.print("Enter vehicle license plate to delete: ");
        String licensePlate = "'" + scanner.next() + "'";
        String formattedDelete = "delete(\"vehicles\", \"license_plate\", " + licensePlate + ")";
        System.out.println("Formatted Delete Command: " + formattedDelete);
    }

    // Placeholder methods to read Parking Lots and Vehicles
    private static void readParkingLots() {
        System.out.println("Read Parking Lots: [This is a test placeholder]");
    }

    private static void readVehicles() {
        System.out.println("Read Vehicles: [This is a test placeholder]");
    }
}
