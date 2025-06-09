import tkinter as tk
from tkinter import messagebox

class BankingApp:
    def __init__(self, master):
        self.master = master
        master.title("Banking App")
        self.balance = 0.0

        self.label = tk.Label(master, text="Balance: $0.00", font=('Arial', 14))
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=5)

        self.deposit_btn = tk.Button(master, text="Deposit", command=self.deposit)
        self.deposit_btn.pack(pady=5)

        self.withdraw_btn = tk.Button(master, text="Withdraw", command=self.withdraw)
        self.withdraw_btn.pack(pady=5)

    def deposit(self):
        try:
            amount = float(self.entry.get())
            if amount <= 0:
                raise ValueError
            self.balance += amount
            self.update_balance()
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter a positive number.")

    def withdraw(self):
        try:
            amount = float(self.entry.get())
            if amount <= 0 or amount > self.balance:
                raise ValueError
            self.balance -= amount
            self.update_balance()
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter a valid amount within balance.")

    def update_balance(self):
        self.label.config(text=f"Balance: ${self.balance:.2f}")
        self.entry.delete(0, tk.END)

root = tk.Tk()
app = BankingApp(root)
root.mainloop()

