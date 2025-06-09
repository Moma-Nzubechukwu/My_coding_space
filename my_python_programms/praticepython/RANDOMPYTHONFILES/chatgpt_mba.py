import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QHBoxLayout, QMessageBox, QListWidget)
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt

class LoginScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bank Login")
        self.setFixedSize(360, 300)

        layout = QVBoxLayout()

        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")
        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.check_login)

        layout.addWidget(QLabel("Login to Bank App"))
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def check_login(self):
        if self.username.text() == "user" and self.password.text() == "pass":
            self.accept_login()
        else:
            QMessageBox.warning(self, "Error", "Invalid credentials")

    def accept_login(self):
        self.hide()
        self.dashboard = Dashboard()
        self.dashboard.show()


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bank Dashboard")
        self.setFixedSize(400, 600)
        self.balance = 1000.0

        layout = QVBoxLayout()

        self.balance_label = QLabel(f"Balance: $ {self.balance:.2f}")
        self.balance_label.setFont(QFont("Arial", 16))
        self.balance_label.setAlignment(Qt.AlignCenter)

        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Enter amount")

        self.deposit_button = QPushButton("Deposit")
        self.deposit_button.clicked.connect(self.deposit)

        self.withdraw_button = QPushButton("Withdraw")
        self.withdraw_button.clicked.connect(self.withdraw)

        self.transactions_list = QListWidget()

        layout.addWidget(QLabel("👤 user", alignment=Qt.AlignRight))
        layout.addWidget(self.balance_label)
        layout.addWidget(self.amount_input)
        layout.addWidget(self.deposit_button)
        layout.addWidget(self.withdraw_button)
        layout.addWidget(QLabel("Transactions:"))
        layout.addWidget(self.transactions_list)

        self.setLayout(layout)

    def deposit(self):
        try:
            amount = float(self.amount_input.text())
            if amount > 0:
                self.balance += amount
                self.update_balance()
                self.add_transaction(f"Deposited $ {amount:.2f}")
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid number")

    def withdraw(self):
        try:
            amount = float(self.amount_input.text())
            if 0 < amount <= self.balance:
                self.balance -= amount
                self.update_balance()
                self.add_transaction(f"Withdrew $ {amount:.2f}")
            elif amount > self.balance:
                QMessageBox.warning(self, "Insufficient Funds", "Not enough balance")
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid number")

    def update_balance(self):
        self.balance_label.setText(f"Balance: $ {self.balance:.2f}")

    def add_transaction(self, text):
        self.transactions_list.insertItem(0, text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor("#f4ecff"))
    app.setPalette(palette)
    window = LoginScreen()
    window.show()
    sys.exit(app.exec_())

