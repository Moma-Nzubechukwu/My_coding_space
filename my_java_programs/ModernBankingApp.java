import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.scene.paint.*;
import javafx.scene.text.Font;
import javafx.stage.Stage;

import java.util.ArrayList;

public class ModernBankingApp extends Application {
    private Stage primaryStage;
    private double balance = 1000.0;
    private ArrayList<String> transactions = new ArrayList<>();

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage stage) {
        this.primaryStage = stage;
        showLoginPage();
    }

    private void showLoginPage() {
        VBox loginLayout = new VBox(10);
        loginLayout.setAlignment(Pos.CENTER);
        loginLayout.setPadding(new Insets(20));
        loginLayout.setBackground(new Background(new BackgroundFill(
                new LinearGradient(0, 0, 1, 1, true, CycleMethod.NO_CYCLE,
                        new Stop(0, Color.web("#e0c3fc")),
                        new Stop(1, Color.web("#8ec5fc"))),
                CornerRadii.EMPTY, Insets.EMPTY)));

        Label title = new Label("Welcome Back ✨");
        title.setFont(new Font("Arial", 24));

        TextField usernameField = new TextField();
        usernameField.setPromptText("Username");

        PasswordField passwordField = new PasswordField();
        passwordField.setPromptText("Password");

        Button loginButton = new Button("Login");
        loginButton.setStyle("-fx-background-color: #a18cd1; -fx-text-fill: white;");
        loginButton.setOnAction(e -> {
            if (usernameField.getText().equals("user") && passwordField.getText().equals("pass")) {
                showDashboard();
            } else {
                new Alert(Alert.AlertType.ERROR, "Invalid credentials").showAndWait();
            }
        });

        loginLayout.getChildren().addAll(title, usernameField, passwordField, loginButton);
        primaryStage.setScene(new Scene(loginLayout, 400, 350));
        primaryStage.setTitle("Bank Login");
        primaryStage.show();
    }

    private void showDashboard() {
        VBox dashboardLayout = new VBox(10);
        dashboardLayout.setPadding(new Insets(20));
        dashboardLayout.setBackground(new Background(new BackgroundFill(
                new LinearGradient(0, 0, 1, 1, true, CycleMethod.NO_CYCLE,
                        new Stop(0, Color.web("#8ec5fc")),
                        new Stop(1, Color.web("#e0c3fc"))),
                CornerRadii.EMPTY, Insets.EMPTY)));

        Label balanceLabel = new Label("$" + String.format("%.2f", balance));
        balanceLabel.setFont(new Font("Arial", 24));
        balanceLabel.setTextFill(Color.WHITE);
        balanceLabel.setAlignment(Pos.CENTER);

        Label subtitle = new Label("Account Balance");
        subtitle.setTextFill(Color.WHITE);

        TextField amountField = new TextField();
        amountField.setPromptText("Enter amount");

        Button depositButton = new Button("Deposit");
        depositButton.setStyle("-fx-background-color: #6a82fb; -fx-text-fill: white;");
        depositButton.setOnAction(e -> {
            try {
                double amount = Double.parseDouble(amountField.getText());
                if (amount > 0) {
                    balance += amount;
                    balanceLabel.setText("$" + String.format("%.2f", balance));
                    transactions.add("Deposited $" + amount);
                    updateTransactionsList();
                }
            } catch (NumberFormatException ex) {
                new Alert(Alert.AlertType.ERROR, "Enter a valid number").showAndWait();
            }
        });

        Button withdrawButton = new Button("Withdraw");
        withdrawButton.setStyle("-fx-background-color: #fc5185; -fx-text-fill: white;");
        withdrawButton.setOnAction(e -> {
            try {
                double amount = Double.parseDouble(amountField.getText());
                if (amount > 0 && amount <= balance) {
                    balance -= amount;
                    balanceLabel.setText("$" + String.format("%.2f", balance));
                    transactions.add("Withdrew $" + amount);
                    updateTransactionsList();
                } else {
                    new Alert(Alert.AlertType.WARNING, "Insufficient funds").showAndWait();
                }
            } catch (NumberFormatException ex) {
                new Alert(Alert.AlertType.ERROR, "Enter a valid number").showAndWait();
            }
        });

        ListView<String> transactionList = new ListView<>();
        transactionList.setId("transactions");
        dashboardLayout.getChildren().addAll(new Label("👩‍💼 user"), balanceLabel, subtitle,
                amountField, depositButton, withdrawButton,
                new Label("Recent Transactions:"), transactionList);

        primaryStage.setScene(new Scene(dashboardLayout, 420, 640));
        primaryStage.setTitle("Bank Dashboard");
        primaryStage.show();
    }

    private void updateTransactionsList() {
        ListView<String> listView = (ListView<String>) ((VBox) primaryStage.getScene().getRoot()).lookup("#transactions");
        listView.getItems().clear();
        listView.getItems().addAll(transactions);
    }
}

