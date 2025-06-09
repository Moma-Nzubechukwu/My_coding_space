import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QHBoxLayout, QMessageBox, QListWidget)
from PyQt5.QtGui import QFont, QColor, QPalette, QLinearGradient, QBrush, QPainter, QPixmap
from PyQt5.QtCore import Qt, QRect

class GradientWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)

    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0, QColor("#e0c3fc"))
        gradient.setColorAt(1, QColor("#8ec5fc"))
        painter.fillRect(self.rect(), QBrush(gradient))

class LoginScreen(GradientWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bank Login")
        self.setFixedSize(400, 350)

        layout = QVBoxLayout()

        title = QLabel("Welcome Back ✨")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")
        self.username.setStyleSheet("padding:10px; border-radius:10px;")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet("padding:10px; border-radius:10px;")

        self.login_button = QPushButton("Login")
        self.login_button.setStyleSheet("background:#a18cd1; color:white; padding:10px; border-radius:10px;")
        self.login_button.clicked.connect(self.check_login)

        layout.addWidget(title)
        layout.addSpacing(20)
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

class Dashboard(GradientWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bank Dashboard")
        self.setFixedSize(420, 640)
        self.balance = 1000.0

        layout = QVBoxLayout()

        avatar = QLabel("👩‍💼 user")
        avatar.setAlignment(Qt.AlignRight)
        avatar.setStyleSheet("font-size: 14px;")

        self.balance_label = QLabel(f"$ {self.balance:.2f}")
        self.balance_label.setFont(QFont("Arial", 24, QFont.Bold))
        self.balance_label.setAlignment(Qt.AlignCenter)
        self.balance_label.setStyleSheet("color:white; margin:10px;")

        balance_box = QLabel("Account Balance")
        balance_box.setFont(QFont("Arial", 12))
        balance_box.setAlignment(Qt.AlignCenter)
        balance_box.setStyleSheet("color:white;")

        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Enter amount")
        self.amount_input.setStyleSheet("padding:10px; border-radius:10px;")

        self.deposit_button = QPushButton("Deposit")
        self.deposit_button.setStyleSheet("background:#6a82fb; color:white; padding:10px; border-radius:10px;")
        self.deposit_button.clicked.connect(self.deposit)

        self.withdraw_button = QPushButton("Withdraw")
        self.withdraw_button.setStyleSheet("background:#fc5185; color:white; padding:10px; border-radius:10px;")
        self.withdraw_button.clicked.connect(self.withdraw)

        self.transactions_list = QListWidget()
        self.transactions_list.setStyleSheet("background:white; border-radius:10px; padding:5px;")

        layout.addWidget(avatar)
        layout.addWidget(self.balance_label)
        layout.addWidget(balance_box)
        layout.addSpacing(10)
        layout.addWidget(self.amount_input)
        layout.addWidget(self.deposit_button)
        layout.addWidget(self.withdraw_button)
        layout.addSpacing(10)
        layout.addWidget(QLabel("Recent Transactions:"))
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
        self.balance_label.setText(f"$ {self.balance:.2f}")

    def add_transaction(self, text):
        self.transactions_list.insertItem(0, text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = LoginScreen()
    window.show()
    sys.exit(app.exec_())

