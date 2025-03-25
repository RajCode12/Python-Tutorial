class Account:
    def __init__(self, acc_number, holder_name, balance):
        self.acc_number = acc_number
        self.holder_name = holder_name
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"${amount} deposited. New balance: ${self.__balance}"
        return "Invalid deposit amount."

    def get_balance(self):
        return self.__balance  # Encapsulation (Getter)
    
    def __str__(self):
        return f"(accountNumber:{self.acc_number}, name:{self.holder_name},balance:{self.__balance})"

# Child class 1: Savings Account
class SavingsAccount(Account):
    def __init__(self, acc_number, holder_name, balance, interest_rate):
        super().__init__(acc_number, holder_name, balance)#call Account class constructor
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return f"Interest Earned: ${super().get_balance() * (self.interest_rate / 100)}"
    
    def __str__(self):
        return f"{super().__str__()},{self.interest_rate}"

# Child class 2: Current Account
class CurrentAccount(Account):
    def __init__(self, acc_number, holder_name, balance, overdraft_limit):
        super().__init__(acc_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit
    
    def calculate_interest(self):
        return f"Interest Earned: ${800}"
    
    def __str__(self):
        return f"{super().__str__()},{self.overdraft_limit}"
    

# Creating accounts
savings = SavingsAccount(1010001, "Anay", 500000, 5.8)
print(savings)
print(savings.calculate_interest())
current = CurrentAccount(1010002, "Joy", 200000, 1000)
print(current)
print(current.calculate_interest())

print(savings.deposit(1000))
print(savings.get_balance())


