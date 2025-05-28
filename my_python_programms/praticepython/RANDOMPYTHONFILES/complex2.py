import json
import getpass
import hashlib

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self._hash_password(password)
        self.accounts = {}

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        return self.password == self._hash_password(password)

    def add_account(self, account_number, account_type, balance):
        self.accounts[account_number] = {
            "account_type": account_type,
            "balance": balance,
            "transactions": []
        }

    def get_account(self, account_number):
        return self.accounts.get(account_number)

class Bank:
    def __init__(self, data_file):
        self.data_file = data_file
        self.users = self._load_users()

    def _load_users(self):
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                users = {}
                for username, user_data in data.items():
                    user = User(username, "")
                    user.password = user_data["password"]
                    user.accounts = user_data["accounts"]
                    users[username] = user
                return users
        except FileNotFoundError:
            return {}

    def _save_users(self):
        data = {}
        for username, user in self.users.items():
            data[username] = {
                "password": user.password,
                "accounts": user.accounts
            }
        with open(self.data_file, "w") as f:
            json.dump(data, f)

    def create_user(self, username, password):
        if username in self.users:
            print("Username already exists.")
            return
        self.users[username] = User(username, password)
        self._save_users()
        print("User created successfully.")

    def authenticate_user(self, username, password):
        user = self.users.get(username)
        if user and user.check_password(password):
            return user
        return None

    def add_account(self, user, account_number, account_type, balance):
        user.add_account(account_number, account_type, balance)
        self._save_users()
        print("Account added successfully.")

    def deposit. You can withdraw money from your account.
        account = user.get_account(account_number)
        if account:
            account["balance"] += amount
            account["transactions"].append({"type": "deposit", "amount": amount})
            self._save_users()
            print("Deposit successful.")
        else:
            print("Account not found.")

    def withdraw(self, user, account_number, amount):
        account = user.get_account(account_number)
        if account:
            if account["balance"] >= amount:
                account["balance"] -= amount
                account["transactions"].append({"type": "withdrawal", "amount": amount})
                self._save_users()
                print("Withdrawal successful.")
            else:
                print("Insufficient balance.")
        else:
            print("Account not found.")

    def check_balance(self, user, account_number):
        account = user.get_account(account_number)
        if account:
            print(f"Balance: {account['balance']}")
        else:
            print("Account not found.")

    def transfer(self, user, from_account_number, to_account_number, amount):
        from_account = user.get_account(from_account_number)
        to_account = user.get_account(to_account_number)
        if from_account and to_account:
            if from_account["balance"] >= amount:
                from_account["balance"] -= amount
                from_account["transactions"].append({"type": "transfer", "amount": amount, "to_account": to_account_number})
                to_account["balance"] += amount
                to_account["transactions"].append({"type": "transfer", "amount": amount, "from_account": from_account_number})
                self._save_users()
                print("Transfer successful.")
            else:
                print("Insufficient balance.")
        else:
            print("One or both accounts not found.")

def main():
    bank = Bank("bank_data.json")

    while True:
        print("\nBanking System Menu:")
        print("1. Create user")
        print("2. Login")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            bank.create_user(username, password)
        elif
