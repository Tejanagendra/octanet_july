import time

print("=======Welcome to the ATM=======")
time.sleep(1)
print("=======Please insert your CARD=======")
time.sleep(2)

password = 4114
pin = int(input("Please enter your 4 digit pin : "))
balance = 6900
transaction_history = []

if pin == password:
    while True:
        print("\n========== ATM Menu ==========")
        print("""choose an option :
                    1. Check Balance
                    2. Withdraw Cash
                    3. Deposit Cash
                    4. Change PIN
                    5. Transaction History
                    6. Exit""")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            # Check Balance
            print(f"Current Balance: {balance}")


        elif choice == '2':
            # Withdraw Cash
            try:
                amount = float(input("Enter amount to withdraw: "))
                if amount > 0 and balance >= amount:
                    balance -= amount
                    transaction_history.append(f'Withdrawal:{amount}')
                    print(f"Withdrawn: {amount}")
                    print(f"Current Balance: {balance}")
                else:
                    print("Withdrawal failed. Insufficient balance.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")


        elif choice == '3':
            # Deposit Cash
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount > 0:
                    balance += amount
                    transaction_history.append(f'Deposit: {amount}')
                    print(f"Deposited: {amount}")
                    print(f"Current Balance: {balance}")
                else:
                    print("Deposit failed. Please enter a valid amount.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")


        elif choice == '4':
            # Change PIN
            new_pin = input("Enter new PIN (4 digits): ")
            if len(new_pin) == 4 and new_pin.isdigit():
                pin = new_pin
                print("PIN changed successfully.")
            else:
                print("Invalid PIN. Please enter 4 digits.")


        elif choice == '5':
            # Transaction History
            print("Transaction History:")
            for transaction in transaction_history:
                print(transaction)


        elif choice == '6':
            # Exit
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and6.")
else:
    print("Wrong pin please try again")
