class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number   # public
        self.__balance = balance               # private (name mangling)

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}, new balance: {self.__balance}")
        else:
            print("Deposit must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}, new balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

# Using the class
account = BankAccount("12345", 1000)
print(account.account_number)  # ✅ accessible
# print(account.__balance)     # ❌ AttributeError (private)

print(account.get_balance())   # ✅ get balance safely
account.deposit(500)           # ✅ modifies balance
account.withdraw(200)
