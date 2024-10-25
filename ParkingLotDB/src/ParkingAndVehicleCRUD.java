import java.util.Scanner;

public class ParkingAndVehicleCRUD {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("\n--- Parking Lots and Vehicles CRUD Application ---");
            System.out.println("1. Manage Parking Lots");
            System.out.println("2. Manage Vehicles");
            System.out.println("3. Exit");
            System.out.print("Select an option: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1 -> parkingLotMenu(scanner);
                case 2 -> vehicleMenu(scanner);
                case 3 -> {
                    System.out.println("Exiting program.");
                    return;
                }
                default -> System.out.println("Invalid choice. Try again.");
            }
        }
    }

    private static void parkingLotMenu(Scanner scanner) {
        while (true) {
            System.out.println("\n--- Parking Lot Management ---");
            System.out.println("1. Add Parking Lot");
            System.out.println("2. Read Parking Lots");
            System.out.println("3. Update Parking Lot");
            System.out.println("4. Delete Parking Lot");
            System.out.println("5. Back to Main Menu");
            System.out.print("Select an option: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1 -> addParkingLot(scanner);
                case 2 -> readParkingLots();
                case 3 -> updateParkingLot(scanner);
                case 4 -> deleteParkingLot(scanner);
                case 5 -> { return; }
                default -> System.out.println("Invalid choice. Try again.");
            }
        }
    }

    private static void vehicleMenu(Scanner scanner) {
        while (true) {
            System.out.println("\n--- Vehicle Management ---");
            System.out.println("1. Add Vehicle");
            System.out.println("2. Read Vehicles");
            System.out.println("3. Update Vehicle");
            System.out.println("4. Delete Vehicle");
            System.out.println("5. Back to Main Menu");
            System.out.print("Select an option: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1 -> addVehicle(scanner);
                case 2 -> readVehicles();
                case 3 -> updateVehicle(scanner);
                case 4 -> deleteVehicle(scanner);
                case 5 -> { return; }
                default -> System.out.println("Invalid choice. Try again.");
            }
        }
    }

    // Placeholder methods for Parking Lot operations
    private static void addParkingLot(Scanner scanner) {
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
        
        System.out.println("Parking lot added: " + name + ", " + street + ", " + city + ", " + state + ", " + zip + ", " + capacity);
    }

    private static void readParkingLots() {
        System.out.println("Read Parking Lots: [This is a test placeholder]");
    }

    private static void updateParkingLot(Scanner scanner) {
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
        
        System.out.println("Parking lot updated: ID " + id + " with new info: " + name + ", " + street + ", " + city + ", " + state + ", " + zip + ", " + capacity);
    }

    private static void deleteParkingLot(Scanner scanner) {
        System.out.print("Enter parking lot ID to delete: ");
        int id = scanner.nextInt();
        System.out.println("Parking lot with ID " + id + " deleted.");
    }

    // Placeholder methods for Vehicle operations
    private static void addVehicle(Scanner scanner) {
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
        
        System.out.println("Vehicle added: " + licensePlate + ", " + state + ", " + color + ", " + make + ", " + model);
    }

    private static void readVehicles() {
        System.out.println("Read Vehicles: [This is a test placeholder]");
    }

    private static void updateVehicle(Scanner scanner) {
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
        
        System.out.println("Vehicle updated: " + licensePlate + " with new info: " + state + ", " + color + ", " + make + ", " + model);
    }

    private static void deleteVehicle(Scanner scanner) {
        System.out.print("Enter vehicle license plate to delete: ");
        String licensePlate = scanner.next();
        System.out.println("Vehicle with license plate " + licensePlate + " deleted.");
    }
}
