import tkinter as tk
from tkinter import messagebox

# Hardcoded credentials
USERNAME = "user"
PASSWORD = "pass"

class BankingApp:
    def __init__(self, master):
        self.master = master
        master.title("Banking App")
        self.balance = 0.0

        self.login_frame = tk.Frame(master)
        self.bank_frame = tk.Frame(master)

        self.create_login_screen()
        self.create_bank_screen()

        self.login_frame.pack()

    def create_login_screen(self):
        tk.Label(self.login_frame, text="Login", font=('Arial', 16)).pack(pady=10)

        tk.Label(self.login_frame, text="Username").pack()
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack(pady=2)

        tk.Label(self.login_frame, text="Password").pack()
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack(pady=2)

        self.login_btn = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_btn.pack(pady=10)

    def create_bank_screen(self):
        self.balance_label = tk.Label(self.bank_frame, text="Balance: $0.00", font=('Arial', 14))
        self.balance_label.pack(pady=10)

        self.amount_entry = tk.Entry(self.bank_frame)
        self.amount_entry.pack(pady=5)

        self.deposit_btn = tk.Button(self.bank_frame, text="Deposit", command=self.deposit)
        self.deposit_btn.pack(pady=2)

        self.withdraw_btn = tk.Button(self.bank_frame, text="Withdraw", command=self.withdraw)
        self.withdraw_btn.pack(pady=2)

        self.logout_btn = tk.Button(self.bank_frame, text="Logout", command=self.logout)
        self.logout_btn.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == USERNAME and password == PASSWORD:
            self.login_frame.pack_forget()
            self.bank_frame.pack()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def logout(self):
        self.bank_frame.pack_forget()
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.login_frame.pack()

    def deposit(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                raise ValueError
            self.balance += amount
            self.update_balance()
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter a positive number.")

    def withdraw(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0 or amount > self.balance:
                raise ValueError
            self.balance -= amount
            self.update_balance()
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter a valid amount within balance.")

    def update_balance(self):
        self.balance_label.config(text=f"Balance: ${self.balance:.2f}")
        self.amount_entry.delete(0, tk.END)

root = tk.Tk()
app = BankingApp(root)
root.mainloop()

