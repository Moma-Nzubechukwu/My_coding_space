// bankingSystem.js

class BankAccount {
    constructor(accountNumber, accountHolder, balance = 0) {
        this.accountNumber = accountNumber;
        this.accountHolder = accountHolder;
        this.balance = balance;
    }

    deposit(amount) {
        if (amount > 0) {
            this.balance += amount;
            console.log(`Deposited $${amount}. New balance: $${this.balance}`);
        } else {
            console.log("Invalid deposit amount.");
        }
    }

    withdraw(amount) {
        if (amount > 0 && amount <= this.balance) {
            this.balance -= amount;
            console.log(`Withdrew $${amount}. New balance: $${this.balance}`);
        } else {
            console.log("Insufficient funds or invalid withdrawal amount.");
        }
    }

    getBalance() {
        console.log(`Current balance: $${this.balance}`);
    }
}

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

let account;

function createAccount() {
    readline.question('Enter your name: ', (name) => {
        readline.question('Enter your initial deposit: ', (initialDeposit) => {
            const accountNumber = Math.floor(Math.random() * 1000000);
            account = new BankAccount(accountNumber, name, parseFloat(initialDeposit));
            console.log(`Account created successfully! Your account number is ${accountNumber}.`);
            mainMenu();
        });
    });
}

function mainMenu() {
    console.log("\nBanking System Menu:");
    console.log("1. Deposit");
    console.log("2. Withdraw");
    console.log("3. Check Balance");
    console.log("4. Exit");

    readline.question('Choose an option: ', (option) => {
        switch (option) {
            case '1':
                readline.question('Enter amount to deposit: ', (amount) => {
                    account.deposit(parseFloat(amount));
                    mainMenu();
                });
                break;
            case '2':
                readline.question('Enter amount to withdraw: ', (amount) => {
                    account.withdraw(parseFloat(amount));
                    mainMenu();
                });
                break;
            case '3':
                account.getBalance();
                mainMenu();
                break;
            case '4':
                console.log("Goodbye!");
                readline.close();
                break;
            default:
                console.log("Invalid option. Please choose again.");
                mainMenu();
        }
    });
}

createAccount();
