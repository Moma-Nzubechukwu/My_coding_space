import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
from datetime import datetime

class ModernBankingApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SecureBank Mobile")
        self.root.geometry("375x667")  # iPhone-like dimensions
        self.root.configure(bg='#1e3a8a')  # Dark blue background
        self.root.resizable(False, False)
        
        self.accounts_file = "accounts.json"
        self.accounts = self.load_accounts()
        self.current_account = None
        
        self.setup_styles()
        self.create_modern_gui()
        
    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure custom styles
        style.configure('Title.TLabel', 
                       background='#1e3a8a', 
                       foreground='white', 
                       font=('SF Pro Display', 24, 'bold'))
        
        style.configure('Subtitle.TLabel', 
                       background='#1e3a8a', 
                       foreground='#93c5fd', 
                       font=('SF Pro Display', 12))
        
        style.configure('Modern.TButton',
                       background='#3b82f6',
                       foreground='white',
                       font=('SF Pro Display', 12, 'bold'),
                       borderwidth=0,
                       focuscolor='none')
        
        style.map('Modern.TButton',
                 background=[('active', '#2563eb')])
        
        style.configure('Card.TFrame',
                       background='white',
                       relief='flat',
                       borderwidth=1)
        
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
    
    def create_modern_gui(self):
        # Main container
        main_frame = tk.Frame(self.root, bg='#1e3a8a')
        main_frame.pack(fill='both', expand=True, padx=0, pady=0)
        
        # Header
        header_frame = tk.Frame(main_frame, bg='#1e3a8a', height=100)
        header_frame.pack(fill='x', pady=(20, 0))
        header_frame.pack_propagate(False)
        
        # Bank logo/name
        logo_label = tk.Label(header_frame, text="🏦 SecureBank", 
                             font=('SF Pro Display', 20, 'bold'),
                             bg='#1e3a8a', fg='white')
        logo_label.pack(pady=10)
        
        subtitle_label = tk.Label(header_frame, text="Mobile Banking", 
                                 font=('SF Pro Display', 12),
                                 bg='#1e3a8a', fg='#93c5fd')
        subtitle_label.pack()
        
        # Content area
        self.content_frame = tk.Frame(main_frame, bg='#f8fafc')
        self.content_frame.pack(fill='both', expand=True, pady=(20, 0))
        
        self.create_login_screen()
    
    def create_login_screen(self):
        # Clear content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Login card
        login_card = tk.Frame(self.content_frame, bg='white', padx=30, pady=30)
        login_card.pack(fill='x', padx=20, pady=30)
        
        # Add shadow effect (simple border)
        shadow_frame = tk.Frame(self.content_frame, bg='#e2e8f0', height=2)
        shadow_frame.place(in_=login_card, x=2, y=2, relwidth=1, relheight=1)
        login_card.lift()
        
        # Welcome text
        welcome_label = tk.Label(login_card, text="Welcome Back", 
                                font=('SF Pro Display', 18, 'bold'),
                                bg='white', fg='#1f2937')
        welcome_label.pack(pady=(0, 5))
        
        desc_label = tk.Label(login_card, text="Sign in to your account", 
                             font=('SF Pro Display', 12),
                             bg='white', fg='#6b7280')
        desc_label.pack(pady=(0, 25))
        
        # Account number field
        tk.Label(login_card, text="Account Number", 
                font=('SF Pro Display', 12, 'bold'),
                bg='white', fg='#374151').pack(anchor='w', pady=(0, 5))
        
        self.account_entry = tk.Entry(login_card, font=('SF Pro Display', 14),
                                     bg='#f9fafb', fg='#111827',
                                     relief='solid', borderwidth=1,
                                     highlightthickness=2,
                                     highlightcolor='#3b82f6')
        self.account_entry.pack(fill='x', pady=(0, 15), ipady=12)
        
        # PIN field
        tk.Label(login_card, text="PIN", 
                font=('SF Pro Display', 12, 'bold'),
                bg='white', fg='#374151').pack(anchor='w', pady=(0, 5))
        
        self.pin_entry = tk.Entry(login_card, font=('SF Pro Display', 14),
                                 bg='#f9fafb', fg='#111827',
                                 relief='solid', borderwidth=1,
                                 show='•', highlightthickness=2,
                                 highlightcolor='#3b82f6')
        self.pin_entry.pack(fill='x', pady=(0, 25), ipady=12)
        
        # Login button
        login_btn = tk.Button(login_card, text="Sign In", 
                             font=('SF Pro Display', 14, 'bold'),
                             bg='#3b82f6', fg='white',
                             relief='flat', borderwidth=0,
                             command=self.login, cursor='hand2')
        login_btn.pack(fill='x', pady=(0, 15), ipady=15)
        
        # Create account button
        create_btn = tk.Button(login_card, text="Create New Account", 
                              font=('SF Pro Display', 12),
                              bg='white', fg='#3b82f6',
                              relief='flat', borderwidth=1,
                              command=self.create_account, cursor='hand2')
        create_btn.pack(fill='x', ipady=12)
        
        # Bind enter key
        self.root.bind('<Return>', lambda e: self.login())
    
    def create_dashboard(self):
        # Clear content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Account overview card
        overview_card = tk.Frame(self.content_frame, bg='white', padx=25, pady=25)
        overview_card.pack(fill='x', padx=20, pady=(20, 10))
        
        # Account info
        account_label = tk.Label(overview_card, text=f"Account •••• {self.current_account[-4:]}", 
                                font=('SF Pro Display', 14),
                                bg='white', fg='#6b7280')
        account_label.pack(anchor='w')
        
        # Balance display
        balance = self.accounts[self.current_account]["balance"]
        balance_label = tk.Label(overview_card, text=f"${balance:,.2f}", 
                                font=('SF Pro Display', 32, 'bold'),
                                bg='white', fg='#111827')
        balance_label.pack(anchor='w', pady=(5, 0))
        
        available_label = tk.Label(overview_card, text="Available Balance", 
                                  font=('SF Pro Display', 12),
                                  bg='white', fg='#6b7280')
        available_label.pack(anchor='w')
        
        # Quick actions
        actions_card = tk.Frame(self.content_frame, bg='white', padx=25, pady=25)
        actions_card.pack(fill='x', padx=20, pady=10)
        
        actions_title = tk.Label(actions_card, text="Quick Actions", 
                                font=('SF Pro Display', 16, 'bold'),
                                bg='white', fg='#111827')
        actions_title.pack(anchor='w', pady=(0, 15))
        
        # Amount input
        tk.Label(actions_card, text="Amount", 
                font=('SF Pro Display', 12, 'bold'),
                bg='white', fg='#374151').pack(anchor='w', pady=(0, 5))
        
        self.amount_entry = tk.Entry(actions_card, font=('SF Pro Display', 16),
                                    bg='#f9fafb', fg='#111827',
                                    relief='solid', borderwidth=1,
                                    highlightthickness=2,
                                    highlightcolor='#3b82f6')
        self.amount_entry.pack(fill='x', pady=(0, 20), ipady=12)
        
        # Action buttons
        buttons_frame = tk.Frame(actions_card, bg='white')
        buttons_frame.pack(fill='x')
        
        deposit_btn = tk.Button(buttons_frame, text="💰 Deposit", 
                               font=('SF Pro Display', 12, 'bold'),
                               bg='#10b981', fg='white',
                               relief='flat', borderwidth=0,
                               command=self.deposit, cursor='hand2')
        deposit_btn.pack(side='left', fill='x', expand=True, padx=(0, 5), ipady=12)
        
        withdraw_btn = tk.Button(buttons_frame, text="💳 Withdraw", 
                                font=('SF Pro Display', 12, 'bold'),
                                bg='#ef4444', fg='white',
                                relief='flat', borderwidth=0,
                                command=self.withdraw, cursor='hand2')
        withdraw_btn.pack(side='right', fill='x', expand=True, padx=(5, 0), ipady=12)
        
        # Logout button
        logout_card = tk.Frame(self.content_frame, bg='white', padx=25, pady=20)
        logout_card.pack(fill='x', padx=20, pady=10)
        
        logout_btn = tk.Button(logout_card, text="Sign Out", 
                              font=('SF Pro Display', 12),
                              bg='white', fg='#6b7280',
                              relief='flat', borderwidth=1,
                              command=self.logout, cursor='hand2')
        logout_btn.pack(fill='x', ipady=12)
    
    def show_modern_message(self, title, message, type_='info'):
        # Custom message dialog
        dialog = tk.Toplevel(self.root)
        dialog.title(title)
        dialog.geometry("300x200")
        dialog.configure(bg='white')
        dialog.resizable(False, False)
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center the dialog
        dialog.geometry("+%d+%d" % (self.root.winfo_rootx() + 50, 
                                   self.root.winfo_rooty() + 100))
        
        # Icon and message
        icon = "✅" if type_ == 'success' else "❌" if type_ == 'error' else "ℹ️"
        
        icon_label = tk.Label(dialog, text=icon, font=('Arial', 24),
                             bg='white')
        icon_label.pack(pady=(20, 10))
        
        title_label = tk.Label(dialog, text=title, 
                              font=('SF Pro Display', 14, 'bold'),
                              bg='white', fg='#111827')
        title_label.pack(pady=(0, 5))
        
        msg_label = tk.Label(dialog, text=message, 
                            font=('SF Pro Display', 12),
                            bg='white', fg='#6b7280')
        msg_label.pack(pady=(0, 20))
        
        ok_btn = tk.Button(dialog, text="OK", 
                          font=('SF Pro Display', 12, 'bold'),
                          bg='#3b82f6', fg='white',
                          relief='flat', borderwidth=0,
                          command=dialog.destroy)
        ok_btn.pack(pady=(0, 20), padx=50, fill='x', ipady=8)
    
    def create_account(self):
        account_num = self.account_entry.get().strip()
        pin = self.pin_entry.get().strip()
        
        if not account_num or not pin:
            self.show_modern_message("Error", "Please enter account number and PIN", 'error')
            return
        
        if account_num in self.accounts:
            self.show_modern_message("Error", "Account already exists", 'error')
            return
        
        self.accounts[account_num] = {"pin": pin, "balance": 0.0, "created": str(datetime.now())}
        self.save_accounts()
        self.show_modern_message("Success", "Account created successfully!", 'success')
        
    def login(self):
        account_num = self.account_entry.get().strip()
        pin = self.pin_entry.get().strip()
        
        if not account_num or not pin:
            self.show_modern_message("Error", "Please enter account number and PIN", 'error')
            return
        
        if account_num not in self.accounts:
            self.show_modern_message("Error", "Account not found", 'error')
            return
        
        if self.accounts[account_num]["pin"] != pin:
            self.show_modern_message("Error", "Invalid PIN", 'error')
            return
        
        self.current_account = account_num
        self.create_dashboard()
        
    def deposit(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                self.show_modern_message("Error", "Amount must be positive", 'error')
                return
            
            self.accounts[self.current_account]["balance"] += amount
            self.save_accounts()
            self.create_dashboard()  # Refresh dashboard
            self.show_modern_message("Success", f"Deposited ${amount:.2f}", 'success')
            
        except ValueError:
            self.show_modern_message("Error", "Please enter a valid amount", 'error')
    
    def withdraw(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                self.show_modern_message("Error", "Amount must be positive", 'error')
                return
            
            current_balance = self.accounts[self.current_account]["balance"]
            if amount > current_balance:
                self.show_modern_message("Error", "Insufficient funds", 'error')
                return
            
            self.accounts[self.current_account]["balance"] -= amount
            self.save_accounts()
            self.create_dashboard()  # Refresh dashboard
            self.show_modern_message("Success", f"Withdrew ${amount:.2f}", 'success')
            
        except ValueError:
            self.show_modern_message("Error", "Please enter a valid amount", 'error')
    
    def logout(self):
        self.current_account = None
        self.create_login_screen()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ModernBankingApp()
    app.run()
