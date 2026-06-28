print("*" * 50)
print("Welcome To My Smart ATM Simulator System")
print("*" * 50)

Name = input("Enter Your Name: ").strip().capitalize()
pin = int(input("Enter Your PIN: "))

balance = 5000
correct_pin = 1234

if pin != correct_pin:
    print("Incorrect Password, The operation was rejected")

else:
    print("The password is correct")
    print("You can write the first letter of the word or the whole word")
    print("The First Option Is Withdraw")
    print("The Second Option Is Check Balance")

    operation = input("Enter Your Choice: ").strip().capitalize()

    if operation == "Check Balance":
        print(f"Your Balance is {balance}")

    elif operation == "Withdraw":
        withdraw = int(input("Enter the amount you want to withdraw: "))

        if withdraw > balance:
            print("You cannot withdraw more than you have")
        else:
            balance -= withdraw
            print("The operation was completed successfully.")
            print(f"Your remaining balance is: {balance}")

    else:
        print("Invalid Input")