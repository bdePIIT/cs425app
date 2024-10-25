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

    // Placeholder method to add a Parking Lot (Currently just displays user input)
    private static void addParkingLot(Scanner scanner) {
        // Prompt user for details about the parking lot
        System.out.print("Enter parking lot name: ");
        String name = scanner.next();
        System.out.print("Enter street: ");
        String street = scanner.next();
        System.out.print("Enter city: ");
        String city = scanner.next();
        System.out.print("Enter state: ");
        String state = scanner.next();
        System.out.print("Enter zip code: ");
        String zip = scanner.next();
        System.out.print("Enter capacity: ");
        int capacity = scanner.nextInt();
        
        // Display the information entered
        System.out.println("Parking lot added: " + name + ", " + street + ", " + city + ", " + state + ", " + zip + ", " + capacity);
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
        String name = scanner.next();
        System.out.print("Enter new street: ");
        String street = scanner.next();
        System.out.print("Enter new city: ");
        String city = scanner.next();
        System.out.print("Enter new state: ");
        String state = scanner.next();
        System.out.print("Enter new zip code: ");
        String zip = scanner.next();
        System.out.print("Enter new capacity: ");
        int capacity = scanner.nextInt();
        
        // Display the information updated
        System.out.println("Parking lot updated: ID " + id + " with new info: " + name + ", " + street + ", " + city + ", " + state + ", " + zip + ", " + capacity);
    }

    // Placeholder method to delete a Parking Lot (Currently just displays the ID entered)
    private static void deleteParkingLot(Scanner scanner) {
        // Prompt user for the parking lot ID to delete
        System.out.print("Enter parking lot ID to delete: ");
        int id = scanner.nextInt();
        System.out.println("Parking lot with ID " + id + " deleted.");
    }

    // Placeholder method to add a Vehicle (Currently just displays user input)
    private static void addVehicle(Scanner scanner) {
        // Prompt user for details about the vehicle
        System.out.print("Enter vehicle license plate: ");
        String licensePlate = scanner.next();
        System.out.print("Enter state: ");
        String state = scanner.next();
        System.out.print("Enter color: ");
        String color = scanner.next();
        System.out.print("Enter make: ");
        String make = scanner.next();
        System.out.print("Enter model: ");
        String model = scanner.next();
        
        // Display the information entered
        System.out.println("Vehicle added: " + licensePlate + ", " + state + ", " + color + ", " + make + ", " + model);
    }

    // Placeholder method to read Vehicles (Just prints a placeholder message for now)
    private static void readVehicles() {
        System.out.println("Read Vehicles: [This is a test placeholder]");
    }

    // Placeholder method to update a Vehicle (Currently just displays user input)
    private static void updateVehicle(Scanner scanner) {
        // Prompt user for details about the vehicle to update
        System.out.print("Enter vehicle license plate to update: ");
        String licensePlate = scanner.next();
        System.out.print("Enter new state: ");
        String state = scanner.next();
        System.out.print("Enter new color: ");
        String color = scanner.next();
        System.out.print("Enter new make: ");
        String make = scanner.next();
        System.out.print("Enter new model: ");
        String model = scanner.next();
        
        // Display the information updated
        System.out.println("Vehicle updated: " + licensePlate + " with new info: " + state + ", " + color + ", " + make + ", " + model);
    }

    // Placeholder method to delete a Vehicle (Currently just displays the license plate entered)
    private static void deleteVehicle(Scanner scanner) {
        // Prompt user for the vehicle license plate to delete
        System.out.print("Enter vehicle license plate to delete: ");
        String licensePlate = scanner.next();
        System.out.println("Vehicle with license plate " + licensePlate + " deleted.");
    }
}
