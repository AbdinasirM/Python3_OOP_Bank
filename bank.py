import random
import datetime


class Bank:
    def __init__(self):
        # Initialize attributes for bank account
        self.name = ''
        self.accountNumber = 0
        self.id = 0
        self.checkingAccount = 0
        self.dateCreatedAccount = None
        self.dateDepositedToAccount = None
        self.dateWithdrawnFromAccount = None
        self.registered = False  # Flag indicating if user is registered

    # Get the current datetime and format it as YYYY-MM-DD
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d")
    now = formatted_datetime  # Current date

    def registerAccount(self, fullname, social_security):
        # Register a new bank account
        self.name = fullname
        self.id = social_security
        self.checkingAccount = 0
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        self.dateCreatedAccount = formatted_datetime
        # Generate a unique account number
        self.accountNumber = self.generate_account_number()
        self.registered = True  # Mark the user as registered

    def generate_account_number(self):
        # Generate a unique account number using random numbers
        random_numbers = [random.randint(1, 100) for _ in range(10)]
        return "".join(map(str, random_numbers))

    def depositMoney(self, money):
        if self.registered:
            # Deposit money into the account
            self.checkingAccount += money
            current_datetime = datetime.datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            self.dateDepositedToAccount = formatted_datetime
        else:
            print("You must be registered to deposit.")

    def withdrawMoney(self, money):
        if self.registered:
            if self.checkingAccount > 0:  # Only allow withdrawals if balance is greater than zero
                if self.checkingAccount >= money:
                    # Withdraw money from the account
                    self.checkingAccount -= money
                    current_datetime = datetime.datetime.now()
                    formatted_datetime = current_datetime.strftime(
                        "%Y-%m-%d %H:%M:%S")
                    self.dateWithdrawnFromAccount = formatted_datetime
                    return self.checkingAccount
                else:
                    return f"You don't have sufficient funds for this withdrawal.\nYour account balance is ${self.checkingAccount}"
            else:
                return "Your account balance is zero. Withdrawals are not allowed."
        else:
            return "You must be registered to withdraw."

    def getUserInfo(self):
        if self.registered:
            # Display user's account information
            print(f"Hello {self.name}!\nThank you for banking with us.\nAccount created on: {self.dateCreatedAccount}\nAccount number: {self.accountNumber}\nAccount balance: ${self.checkingAccount}\nLast deposit: {self.dateDepositedToAccount}\nLast withdrawal: {self.dateWithdrawnFromAccount}")
        else:
            print("You must be registered to see account information.")
