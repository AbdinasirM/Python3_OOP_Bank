from bank import Bank  # Import the Bank class from the bank module

if __name__ == "__main__":
    bank = Bank()  # Create an instance of the Bank class

    while True:
        # Display the main menu options
        print("1. Register Bank Account")
        print("2. Deposit to your Account")
        print("3. Withdraw from your Account")
        print("4. Get your Bank information and balances")
        print("5. Exit")

        # Get user's choice
        choice = int(
            input("Please enter a number choice from the list above: "))

        if choice == 1:
            # Register a new bank account
            fullname = input("Please enter your full name: ")
            social_security = input("Please enter your social security: ")
            bank.registerAccount(fullname, social_security)
            print("\n")  # Print newline for formatting

        elif choice == 2:
            # Deposit money into the account
            money = float(input("Please enter the amount to deposit: "))
            bank.depositMoney(money)
            print("\n")  # Print newline for formatting

        elif choice == 3:
            # Withdraw money from the account
            money = float(input("Please enter the amount to withdraw: "))
            result = bank.withdrawMoney(money)
            print(result)  # Print the result of the withdrawal
            print("\n")  # Print newline for formatting

        elif choice == 4:
            # Display user's bank information
            print("\n")  # Print newlines for spacing
            bank.getUserInfo()
            print("\n")  # Print newlines for spacing

        elif choice == 5:
            # Exit the program
            print("Thank you for using our banking system. Goodbye!")
            break  # Exit the loop

        else:
            # Invalid choice
            print("Invalid choice. Please select a valid option.")
