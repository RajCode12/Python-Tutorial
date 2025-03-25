try:
    result = 10 / 0
    print('division = ',result)
except ZeroDivisionError as e:
    print(f"Error: {e}")

try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError as e:
    print(f"Error: {e}")

try:
    my_dict = {"name": "Ajay",'age':20,'emailid':'ajay123@gmail.com'}
    print(my_dict["contactnumber"])
except KeyError as e:
    print(f" Key not found : {e}")

try:
    result = "welcome" + 10
except TypeError as e:
    print(f"Error: {e}")

try:
    num = int("abc")
    print(num)
except ValueError as e:
    print(f"Error: {e}")

try:
    my_list = [1, 2, 3]
    my_list.append(4)  # Works
    my_list.upper()  # Lists don't have an 'upper' method
except AttributeError as e:
    print(f"Error: {e}")

try:
    x = int(input("Enter a number: "))  # ValueError if input is not a number
    result = 10 / x  # ZeroDivisionError if x is 0
    my_list = [1, 2, 3]
    print(my_list[7])  # IndexError if index is out of range
except ValueError:
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero!")
except IndexError:
    print("Index out of range!")
except Exception as e:  # General exception (fallback case)
    print(f"An unexpected error occurred: {e}")



class CustomError(Exception):
    """Custom exception for demonstration."""
    def __init__(self, message):
        super().__init__(message)



def check_age(age):
    if age < 18:
        raise CustomError("Age must be 18 or older.")
    print("Access granted!")

try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except CustomError as e:
    print(f"Custom Exception: {e}")
except ValueError:
    print("Invalid input! Please enter a number.")

def divide(a, b):
    if b <= 0:
        raise ZeroDivisionError("You cannot divide by -ve number or zero!")
    return a / b

try:
    result = divide(10, -3)
except ZeroDivisionError as e:
    print(f"Error: {e}")



class NegativeBalanceError(Exception):
    """Custom exception for negative bank balance."""
    def __init__(self, balance):
        super().__init__(f"Balance cannot be negative! Current balance: {balance}")
        self.balance = balance

def withdraw(balance, amount):
    if balance - amount < 0:
        raise NegativeBalanceError(balance - amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
    print(f"New Balance: {new_balance}")
except NegativeBalanceError as e:
    print(f"Custom Exception: {e}")

try:
    x = int(input("Enter a number: "))  # ValueError if input is not a number
    result = 10 / x  # ZeroDivisionError if x is 0
    try:
        my_list = [1, 2, 3]
        print(my_list[5])  # IndexError if index is out of range
    except IndexError:
        print("Index out of range!")
    print('end of outer try block')
except ValueError:
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero!")
except Exception as e:  # General exception (fallback case)
    print(f"An unexpected error occurred: {e}")

