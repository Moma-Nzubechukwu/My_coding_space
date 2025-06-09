import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class BankingApp {
    private static final String USERNAME = "user";
    private static final String PASSWORD = "pass";

    private JFrame frame;
    private JPanel loginPanel, bankPanel;
    private JTextField usernameField, amountField;
    private JPasswordField passwordField;
    private JLabel balanceLabel;
    private double balance = 0.0;

    public BankingApp() {
        frame = new JFrame("Banking App");
        frame.setSize(300, 250);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLocationRelativeTo(null);

        initLoginPanel();
        initBankPanel();

        frame.setContentPane(loginPanel);
        frame.setVisible(true);
    }

    private void initLoginPanel() {
        loginPanel = new JPanel(new GridLayout(5, 1, 5, 5));
        loginPanel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));

        usernameField = new JTextField();
        passwordField = new JPasswordField();

        JButton loginButton = new JButton("Login");
        loginButton.addActionListener(e -> handleLogin());

        loginPanel.add(new JLabel("Username:"));
        loginPanel.add(usernameField);
        loginPanel.add(new JLabel("Password:"));
        loginPanel.add(passwordField);
        loginPanel.add(loginButton);
    }

    private void initBankPanel() {
        bankPanel = new JPanel();
        bankPanel.setLayout(new BoxLayout(bankPanel, BoxLayout.Y_AXIS));
        bankPanel.setBorder(BorderFactory.createEmptyBorder(15, 15, 15, 15));

        balanceLabel = new JLabel("Balance: $0.00");
        balanceLabel.setAlignmentX(Component.CENTER_ALIGNMENT);

        amountField = new JTextField();
        amountField.setMaximumSize(new Dimension(Integer.MAX_VALUE, 30));

        JButton depositButton = new JButton("Deposit");
        depositButton.addActionListener(e -> deposit());

        JButton withdrawButton = new JButton("Withdraw");
        withdrawButton.addActionListener(e -> withdraw());

        JButton logoutButton = new JButton("Logout");
        logoutButton.addActionListener(e -> logout());

        bankPanel.add(balanceLabel);
        bankPanel.add(Box.createRigidArea(new Dimension(0, 10)));
        bankPanel.add(amountField);
        bankPanel.add(Box.createRigidArea(new Dimension(0, 5)));
        bankPanel.add(depositButton);
        bankPanel.add(Box.createRigidArea(new Dimension(0, 5)));
        bankPanel.add(withdrawButton);
        bankPanel.add(Box.createRigidArea(new Dimension(0, 10)));
        bankPanel.add(logoutButton);
    }

    private void handleLogin() {
        String user = usernameField.getText();
        String pass = new String(passwordField.getPassword());

        if (user.equals(USERNAME) && pass.equals(PASSWORD)) {
            frame.setContentPane(bankPanel);
            frame.revalidate();
            frame.repaint();
        } else {
            JOptionPane.showMessageDialog(frame, "Invalid credentials", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void deposit() {
        try {
            double amount = Double.parseDouble(amountField.getText());
            if (amount <= 0) throw new NumberFormatException();
            balance += amount;
            updateBalance();
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(frame, "Enter a valid positive number", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void withdraw() {
        try {
            double amount = Double.parseDouble(amountField.getText());
            if (amount <= 0 || amount > balance) throw new NumberFormatException();
            balance -= amount;
            updateBalance();
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(frame, "Invalid withdrawal amount", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void updateBalance() {
        balanceLabel.setText(String.format("Balance: $%.2f", balance));
        amountField.setText("");
    }

    private void logout() {
        usernameField.setText("");
        passwordField.setText("");
        amountField.setText("");
        frame.setContentPane(loginPanel);
        frame.revalidate();
        frame.repaint();
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(BankingApp::new);
    }
}

