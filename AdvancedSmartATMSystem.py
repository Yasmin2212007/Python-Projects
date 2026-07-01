
print("*" *50)
print("Welcome To My Advanced Smart ATM System ")
print("*" *50)

Name = input("Enter Your Name: ").strip().capitalize()
pin = int(input("Enter Your PIN: "))

correct_pin = 1234
balance = 10000
if pin != correct_pin:
    print("Incorrect Password, The operation was rejected")

else:
    while True:

        print("=" * 40)
        print("ATM MENU")
        print("=" * 40)
        print("1 - Check Balance")
        print("2 - Withdraw")
        print("3 - Deposit")
        print("4 - Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            print(f"\nYour Balance Is: {balance}")

        elif choice == 2:
            amount = int(input("Enter Withdrawal Amount: "))

            if amount <= 0:
                print("Invalid Amount")

            elif amount > balance:
                print("Insufficient Balance")

            else:
                balance -= amount
                print("Withdrawal Successful")
                print(f"Current Balance: {balance}")

        elif choice == 3:
            amount = int(input("Enter Deposit Amount: "))

            if amount <= 0:
                print("Invalid Amount")

            else:
                balance += amount
                print("Deposit Successful")
                print(f"Current Balance: {balance}")

        elif choice == 4:
            print(f"Thank You {Name} For Using Our ATM.")
            break

        else:
            print("Invalid Choice")




























