import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class BasicJDBCConnector {

    public static void main(String[] args) {
        // Database credentials
        String url = "jdbc:mysql://localhost:3306/testdb"; // Replace 'testdb' with your DB name
        String user = "root"; // Replace with your DB username
        String password = "D$ai1919"; // Replace with your DB password

        try {
            // Load MySQL JDBC Driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            // Connect to the database
            Connection conn = DriverManager.getConnection(url, user, password);
            System.out.println("✅ Connected to the database!");

            // Create a statement and execute query
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT NOW()");

            // Print result
            if (rs.next()) {
                System.out.println("Current Time from DB: " + rs.getString(1));
            }

            // Close resources
            rs.close();
            stmt.close();
            conn.close();
            System.out.println("🔒 Connection closed.");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}