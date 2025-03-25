class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount < 0:
            print('cannot deposit ')
        else:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds!")
    def __str__(self):
        return f"(accountNumber:{self.account_number}, balance:{self.__balance})"

account = BankAccount("123456", 1000)# Creating an object
account.deposit(500)
account.withdraw(300)
#print(account.account_number)
