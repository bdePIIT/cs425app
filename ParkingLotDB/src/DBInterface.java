import java.sql.*;
import java.util.ArrayList;

public class DBInterface {
    boolean connected = false;
    private final String url = "jdbc:postgresql://localhost:5432/ParkingLot";
    private final String username = "postgres";
    private Connection con;
    private Statement st;

    public void connect() {
        if (connected) {
            System.out.println("Already connected to database!");
            return;
        }

        try {
            con = DriverManager.getConnection(url, username, "0000");
            st = con.createStatement();
            connected = true;
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void disconnect() {
        if (!connected) {
            System.out.println("Not currently connected to database!");
            return;
        }
        try {
            con.close();
            st = null;
            connected = false;
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void insert(String table, String[] args) {
        if (!connected) {
            System.out.println("Database not connected!");
            return;
        }
        String argFormation = '(' + String.join(", ", args) + ")";
        String query = "insert into " + table + " values " + argFormation + ";";
        try {
            st.executeUpdate(query);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public ArrayList<String[]> readAllRows(String table, String[] cols) {
        if (!connected) {
            System.out.println("Database not connected!");
            return null;
        }
        ArrayList<String[]> result = new ArrayList<>();

        String query = "SELECT " + String.join(",", cols) + " FROM " + table + ";";

        try {
            ResultSet rs;

            rs = st.executeQuery(query);
            while (rs.next()) {
                String[] rowData = new String[cols.length];
                for (int i = 0; i < cols.length; i++) {
                    rowData[i] = rs.getString(i + 1);
                }
                result.add(rowData);
            }
        } catch (SQLException e) {
            System.err.println("Error executing query: " + query);
            e.printStackTrace();
        }
        return result;
    }

    public ArrayList<String[]> read(String table, String[] cols, String condAttr, String attrVal) {
        if (!connected) {
            System.out.println("Database not connected!");
            return null;
        }
        ArrayList<String[]> result = new ArrayList<>();
        String query = "SELECT " + String.join(",", cols) + " FROM " + table + " WHERE " + condAttr + " = " + attrVal
                + ";";

        try {
            ResultSet rs;

            rs = st.executeQuery(query);
            while (rs.next()) {
                String[] rowData = new String[cols.length];
                for (int i = 0; i < cols.length; i++) {
                    rowData[i] = rs.getString(i + 1);
                }
                result.add(rowData);
            }
        } catch (SQLException e) {
            System.err.println("Error executing query: " + query);
            e.printStackTrace();
        }
        return result.isEmpty() ? new ArrayList<>() : result; // Avoids returning null
    }

    public void update(String table, String col, String newVal, String pk, String pkVal) {
        if (!connected) {
            System.out.println("Database not connected!");
            return;
        }
        String query = "UPDATE " + table + " SET " + col + " = " + newVal + " WHERE " + pk + " = " + pkVal + ";";
        try {
            st.executeUpdate(query);
        } catch (SQLException e) {
            System.err.println("Error executing update: " + query);
            e.printStackTrace();
        }
    }

    public void delete(String table, String attr, String val) {
        if (!connected) {
            System.out.println("Database not connected!");
            return;
        }
        String query = "delete from " + table + " where " + attr + " = " + val + ";";
        try {
            st.executeUpdate(query);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

}
