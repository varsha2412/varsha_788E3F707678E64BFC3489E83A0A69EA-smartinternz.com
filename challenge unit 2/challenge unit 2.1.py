class BankAccount:
    def _init_(self, account_number, account_holder_name, initial_balance):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            return f"Deposited {amount} successfully. New balance: {self._account_balance}"
        else:
            return "Invalid deposit amount. Please deposit a positive amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            return f"Withdrew {amount} successfully. New balance: {self._account_balance}"
        elif amount <= 0:
            return "Invalid withdrawal amount. Please withdraw a positive amount."
        else:
            return "Insufficient funds for withdrawal."

    def display_balance(self):
        return f"Account Number: {self._account_number}, Account Holder: {self._account_holder_name}, Balance: {self._account_balance}"

# Testing the BankAccount class
if _name_ == "_main_":
    account = BankAccount("1234567890", "John Doe", 1000.00)
    
    print(account.display_balance())
    print(account.deposit(500.50))
    print(account.withdraw(200.25))
    print(account.display_balance())