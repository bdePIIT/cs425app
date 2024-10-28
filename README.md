Parking and Vehicle CRUD Application
This is a Java-based command-line application for managing parking lots and vehicles. It allows you to perform basic Create, Read, Update, and Delete (CRUD) operations on both parking_lots and vehicles. The application captures user input and formats each operation as a string for further use.

Features:
Main Menu
The main menu provides options to manage either Parking Lots or Vehicles or to exit the application.

Choose 1 for Parking Lot Management
Choose 2 for Vehicle Management
Choose 3 to Exit the application

Parking Lot Management:
Add a new parking lot: Input details like name, street, city, state, zip code, and capacity.
View all parking lots: Displays all stored parking lots with relevant details.
Update details of an existing parking lot: Modify information such as the name, address, or capacity of an existing parking lot.
Delete a parking lot: Remove a parking lot from the database by entering its unique ID.

Vehicle Management:
Add a new vehicle: Input vehicle details such as license plate, state, color, make, and model.
View all vehicles: Displays all stored vehicles with relevant details.
Update details of an existing vehicle: Modify vehicle information such as color, make, model, or associated parking lot.
Delete a vehicle: Remove a vehicle from the database by entering its license plate.

HOW TO USE
Setup:

Compile and run the program.
Navigation:

The main menu will give you two options for managing the database tables:

Parking lots
Vehicles
Select the desired table to manage.

Actions:

For each table, you will be presented with the following prompts:
Create: Add a new entry to the selected table.
Read: View all entries in the table.
Update: Update details of an existing entry.
Delete: Delete an entry from the table.
Back to Main Menu: Return to the main menu to switch between Parking Lots and Vehicles.
Detailed Instructions for Each Action
Selecting Create
Parking lot:

You will be prompted to provide the following information to add a new parking lot to the database:
Enter parking lot name:
Enter street:
Enter city:
Enter state:
Enter zip code:
Enter capacity:

Vehicle:

You will be prompted to enter details such as:
Enter vehicle license plate:
Enter state:
Enter color:
Enter make:
Enter model:

Selecting Read
Displays the entire contents of the selected table, either Parking Lots or Vehicles.
Selecting Update

Parking Lot:
After selecting Update, you will:
Be prompted to enter the unique ID of the parking lot you wish to update.
Then, choose the specific field to update, such as:
Name
Street
City
State
Zip Code
Capacity
Vehicle:

You will be prompted to enter the vehicle’s license plate, then select the specific attribute you wish to update, such as:
State
Color
Make
Model
Parking Lot ID

Selecting Delete
Enter the unique identifier (ID or license plate) of the parking lot or vehicle you wish to delete, and confirm the deletion.
Dependencies
This application requires a database connection through the DBInterface class. Ensure your database is properly set up with tables for parking_lots and vehicles and that the DBInterface class is configured to handle connections and CRUD operations.

Notes
The application checks for the existence of parking lots and vehicles before updates and deletions to prevent errors.
The DBInterface handles all database-related operations, so ensure it has valid methods for connecting, inserting, reading, updating, and deleting records.
