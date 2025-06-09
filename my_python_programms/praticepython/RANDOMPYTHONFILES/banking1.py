import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

class BankingApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simple Banking App")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Load accounts from file
        self.accounts_file = "accounts.json"
        self.accounts = self.load_accounts()
        self.current_account = None
        
        self.create_widgets()
        
    def load_accounts(self):
        if os.path.exists(self.accounts_file):
            try:
                with open(self.accounts_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save_accounts(self):
        with open(self.accounts_file, 'w') as f:
            json.dump(self.accounts, f, indent=2)
    
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Simple Banking System", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Account selection
        ttk.Label(main_frame, text="Account Number:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.account_var = tk.StringVar()
        self.account_entry = ttk.Entry(main_frame, textvariable=self.account_var, width=20)
        self.account_entry.grid(row=1, column=1, pady=5, padx=(10, 0))
        
        # PIN entry
        ttk.Label(main_frame, text="PIN:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.pin_var = tk.StringVar()
        self.pin_entry = ttk.Entry(main_frame, textvariable=self.pin_var, show="*", width=20)
        self.pin_entry.grid(row=2, column=1, pady=5, padx=(10, 0))
        
        # Login button
        login_btn = ttk.Button(main_frame, text="Login", command=self.login)
        login_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Create account button
        create_btn = ttk.Button(main_frame, text="Create New Account", command=self.create_account)
        create_btn.grid(row=4, column=0, columnspan=2, pady=5)
        
        # Banking operations frame (initially hidden)
        self.banking_frame = ttk.LabelFrame(main_frame, text="Banking Operations", padding="10")
        self.banking_frame.grid(row=5, column=0, columnspan=2, pady=20, sticky=(tk.W, tk.E))
        self.banking_frame.grid_remove()  # Hide initially
        
        # Balance display
        self.balance_label = ttk.Label(self.banking_frame, text="Balance: $0.00", 
                                      font=("Arial", 12, "bold"))
        self.balance_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Amount entry
        ttk.Label(self.banking_frame, text="Amount:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.amount_var = tk.StringVar()
        self.amount_entry = ttk.Entry(self.banking_frame, textvariable=self.amount_var, width=15)
        self.amount_entry.grid(row=1, column=1, pady=5, padx=(10, 0))
        
        # Operation buttons
        deposit_btn = ttk.Button(self.banking_frame, text="Deposit", command=self.deposit)
        deposit_btn.grid(row=2, column=0, pady=10, padx=5)
        
        withdraw_btn = ttk.Button(self.banking_frame, text="Withdraw", command=self.withdraw)
        withdraw_btn.grid(row=2, column=1, pady=10, padx=5)
        
        # Logout button
        logout_btn = ttk.Button(self.banking_frame, text="Logout", command=self.logout)
        logout_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
    def create_account(self):
        account_num = self.account_var.get().strip()
        pin = self.pin_var.get().strip()
        
        if not account_num or not pin:
            messagebox.showerror("Error", "Please enter account number and PIN")
            return
        
        if account_num in self.accounts:
            messagebox.showerror("Error", "Account already exists")
            return
        
        self.accounts[account_num] = {"pin": pin, "balance": 0.0}
        self.save_accounts()
        messagebox.showinfo("Success", "Account created successfully!")
        
    def login(self):
        account_num = self.account_var.get().strip()
        pin = self.pin_var.get().strip()
        
        if not account_num or not pin:
            messagebox.showerror("Error", "Please enter account number and PIN")
            return
        
        if account_num not in self.accounts:
            messagebox.showerror("Error", "Account not found")
            return
        
        if self.accounts[account_num]["pin"] != pin:
            messagebox.showerror("Error", "Invalid PIN")
            return
        
        self.current_account = account_num
        self.banking_frame.grid()  # Show banking operations
        self.update_balance_display()
        messagebox.showinfo("Success", f"Welcome, Account {account_num}!")
        
    def update_balance_display(self):
        if self.current_account:
            balance = self.accounts[self.current_account]["balance"]
            self.balance_label.config(text=f"Balance: ${balance:.2f}")
    
    def deposit(self):
        try:
            amount = float(self.amount_var.get())
            if amount <= 0:
                messagebox.showerror("Error", "Amount must be positive")
                return
            
            self.accounts[self.current_account]["balance"] += amount
            self.save_accounts()
            self.update_balance_display()
            self.amount_var.set("")
            messagebox.showinfo("Success", f"Deposited ${amount:.2f}")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")
    
    def withdraw(self):
        try:
            amount = float(self.amount_var.get())
            if amount <= 0:
                messagebox.showerror("Error", "Amount must be positive")
                return
            
            current_balance = self.accounts[self.current_account]["balance"]
            if amount > current_balance:
                messagebox.showerror("Error", "Insufficient funds")
                return
            
            self.accounts[self.current_account]["balance"] -= amount
            self.save_accounts()
            self.update_balance_display()
            self.amount_var.set("")
            messagebox.showinfo("Success", f"Withdrew ${amount:.2f}")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")
    
    def logout(self):
        self.current_account = None
        self.banking_frame.grid_remove()
        self.account_var.set("")
        self.pin_var.set("")
        self.amount_var.set("")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = BankingApp()
    app.run()
