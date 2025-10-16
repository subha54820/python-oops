from abc import ABC, abstractmethod

# 🔹 Abstraction: Account is an abstract base class that defines a common structure.
class Account(ABC):
    def __init__(self, owner, initial_balance=0):
        # 🔹 Encapsulation: Attributes are protected (single underscore)
        self._owner = owner
        self._balance = initial_balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self._balance

# 🔹 Inheritance: SavingsAccount inherits from Account
class SavingsAccount(Account):
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

# 🔹 Inheritance: CheckingAccount inherits from Account
class CheckingAccount(Account):
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

# 🔹 Polymorphism: Works with any Account type
def display_account_info(account):
    print(f"\nAccount Owner: {account._owner}")
    print(f"Current Balance: ₹{account.get_balance()}\n")

# 🔹 Demonstration
if __name__ == "__main__":
    savings = SavingsAccount("Alice", 1000)
    checking = CheckingAccount("Bob", 500)

    print("----- Savings Account -----")
    display_account_info(savings)
    savings.deposit(200)
    savings.withdraw(150)
    print(f"Final Balance: ₹{savings.get_balance()}") 

    print("\n----- Checking Account -----")
    display_account_info(checking)
    checking.deposit(300)
    checking.withdraw(700)
    print(f"Final Balance: ₹{checking.get_balance()}") 
