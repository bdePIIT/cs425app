import java.util.ArrayList;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");

        DBInterface db = new DBInterface();
        db.connect();

        System.out.println("Start\n-----------");
        printArrayList(db.readAllRows("owners", new String[]{"owner_id", "first_name", "last_name"}));
        db.insert("owners", new String[]{"16", "'John'", "'Doe'"});
        System.out.println("Insert\n------------");
        printArrayList(db.readAllRows("owners", new String[]{"owner_id", "first_name", "last_name"}));
        db.update("owners", "last_name", "'Fox'", "owner_id", "16");
        System.out.println("Update\n----------");
        printArrayList(db.readAllRows("owners", new String[]{"owner_id", "first_name", "last_name"}));
        db.delete("owners", "owner_id", "16");
        System.out.println("Delete\n-----------");
        printArrayList(db.readAllRows("owners", new String[]{"owner_id", "first_name", "last_name"}));
        db.disconnect();
        
    }
    
    public static void printArrayList(ArrayList<String[]> list){
        for(String[] sarr : list){
            System.out.println("[" + String.join(",",sarr) + "]");
        }
    }
}
