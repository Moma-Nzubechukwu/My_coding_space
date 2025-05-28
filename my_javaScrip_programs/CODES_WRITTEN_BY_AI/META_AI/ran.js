// User class
class User {
  constructor(id, name, email, password) {
    this.id = id;
    this.name = name;
    this.email = email;
    this.password = password;
    this.accounts = [];
  }

  addAccount(account) {
    this.accounts.push(account);
  }

  removeAccount(accountId) {
    this.accounts = this.accounts.filter(account => account.id !== accountId);
  }
}

// Account class
class Account {
  constructor(id, type, balance) {
    this.id = id;
    this.type = type;
    this.balance = balance;
    this.transactions = [];
  }

  deposit(amount) {
    this.balance += amount;
    this.transactions.push({ type: 'deposit', amount });
  }

  withdraw(amount) {
    if (this.balance >= amount) {
      this.balance -= amount;
      this.transactions.push({ type: 'withdrawal', amount });
    } else {
      throw new Error('Insufficient balance');
    }
  }

  getBalance() {
    return this.balance;
  }

  getTransactions() {
    return this.transactions;
  }
}

// Transaction class
class Transaction {
  constructor(id, type, amount, timestamp) {
    this.id = id;
    this.type = type;
    this.amount = amount;
    this.timestamp = timestamp;
  }
}

// Banking system class
class BankingSystem {
  constructor() {
    this.users = [];
    this.accounts = [];
    this.transactions = [];
  }

  createUser(name, email, password) {
    const user = new User(this.users.length + 1, name, email, password);
    this.users.push(user);
    return user;
  }

  createAccount(userId, type, initialBalance) {
    const user = this.users.find(user => user.id === userId);
    if (user) {
      const account = new Account(this.accounts.length + 1, type, initialBalance);
      user.addAccount(account);
      this.accounts.push(account);
      return account;
    } else {
      throw new Error('User not found');
    }
  }

  deposit(accountId, amount) {
    const account = this.accounts.find(account => account.id === accountId);
    if (account) {
      account.deposit(amount);
    } else {
      throw new Error('Account not found');
    }
  }

  withdraw(accountId, amount) {
    const account = this.accounts.find(account => account.id === accountId);
    if (account) {
      account.withdraw(amount);
    } else {
      throw new Error('Account not found');
    }
  }

  getAccountBalance(accountId) {
    const account = this.accounts.find(account => account.id === accountId);
    if (account) {
      return account.getBalance();
    } else {
      throw new Error('Account not found');
    }
  }

  getAccountTransactions(accountId) {
    const account = this.accounts.find(account => account.id === accountId);
    if (account) {
      return account.getTransactions();
    } else {
      throw new Error('Account not found');
    }
  }
}

// Usage
const bankingSystem = new BankingSystem();
const user = bankingSystem.createUser('John Doe', 'john@example.com', 'password123');
const account = bankingSystem.createAccount(user.id, 'checking', 1000);

bankingSystem.deposit(account.id, 500);
bankingSystem.withdraw(account.id, 200);

console.log(bankingSystem.getAccountBalance(account.id));
console.log(bankingSystem.getAccountTransactions(account.id));

// Additional functionality
class Admin {
  constructor(bankingSystem) {
    this.bankingSystem = bankingSystem;
  }

  viewAllAccounts() {
    return this.bankingSystem.accounts;
  }

  viewAllTransactions() {
    return this.bankingSystem.accounts.reduce((transactions, account) => transactions.concat(account.transactions), []);
  }
}

const admin = new Admin(bankingSystem);
console.log(admin.viewAllAccounts());
console.log(admin.viewAllTransactions());

// More functionality
class Customer {
  constructor(bankingSystem, userId) {
    this.bankingSystem = bankingSystem;
    this.userId = userId;
  }

  viewAccountBalance(accountId) {
    return this.bankingSystem.getAccountBalance(accountId);
  }

  viewAccountTransactions(accountId) {
    return this.bankingSystem.getAccountTransactions(accountId);
  }
}

const customer = new Customer(bankingSystem, user.id);
console.log(customer.viewAccountBalance(account.id));
console.log(customer.viewAccountTransactions(account.id));

// Even more functionality
class TransactionHistory {
  constructor(bankingSystem) {
    this.bankingSystem = bankingSystem;
  }

  getTransactionHistory(accountId) {
    return this.bankingSystem.getAccountTransactions(accountId);
  }
}

const transactionHistory = new TransactionHistory
