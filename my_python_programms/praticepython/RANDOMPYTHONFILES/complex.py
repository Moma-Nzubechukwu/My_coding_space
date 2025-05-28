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
            "balance": balance
        }

    def get_account(self, account_number):
        return self.accounts.get(account_number)

class Bank:
    def __init__(self):
        self.users = {}

    def create_user(self, username, password):
        if username in self.users:
            print("Username already exists.")
            return
        self.users[username] = User(username, password)
        print("User created successfully.")

    def authenticate_user(self, username, password):
        user = self.users.get(username)
        if user and user.check_password(password):
            return user
        return None

    def add_account(self, user, account_number, account_type, balance):
        user.add_account(account_number, account_type, balance)
        print("Account added successfully.")

    def deposit(self, user, account_number, amount):
        account = user.get_account(account_number)
        if account:
            account["balance"] += amount
            print("Deposit successful.")
        else:
            print("Account not found.")

    def withdraw(self, user, account_number, amount):
        account = user.get_account(account_number)
        if account:
            if account["balance"] >= amount:
                account["balance"] -= amount
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

def main():
    bank = Bank()

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
        elif choice == "2":
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            user = bank.authenticate_user(username, password)
            if user:
                while True:
                    print("\nUser Menu:")
                    print("1. Add account")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Check balance")
                    print("5. Logout")

                    user_choice = input("Enter your choice: ")

                    if user_choice == "1":
                        account_number = input("Enter account number: ")
                        account_type = input("Enter account type: ")
                        balance = float(input("Enter initial balance: "))
                        bank.add_account(user, account_number, account_type, balance)
                    elif user_choice == "2":
                        account_number = input("Enter account number: ")
                        amount = float(input("Enter amount to deposit: "))
                        bank.deposit(user, account_number, amount)
                    elif user_choice == "3":
                        account_number = input("Enter account number: ")
                        amount = float(input("Enter amount to withdraw: "))
                        bank.withdraw(user, account_number, amount)
                    elif user_choice == "4":
                        account_number = input("Enter account number: ")
                        bank.check_balance(user, account_number)
                    elif user_choice == "5":
                        break
                    else:
                        print("Invalid choice.")
            else:
                print("Invalid username or password.")
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
