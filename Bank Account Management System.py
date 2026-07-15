accounts = {}

def register():
    print("\n--- Register ---")
    username = input("Enter Username: ").strip()

    if username == "":
        print("Username can't be empty")
        return

    if username in accounts:
        print("This username is already taken")
        return

    password = input("Enter Password: ").strip()
    if len(password) < 6:
        print("Password too short, minimum 6 characters")
        return

    accounts[username] = {"password": password, "balance": 0, "last_transaction": "No transactions yet"}
    print("Done! Account created for", username)


def login():
    print("\n--- Login ---")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username not in accounts or accounts[username]["password"] != password:
        print("Wrong username or password")
        return

    print("Welcome back,", username)
    bank_menu(username)


def bank_menu(username):
    while True:
        print("\n1) Balance  2) Deposit  3) Withdraw  4) Transfer  5) Logout")
        choice = input("Choice: ")

        if choice == "1":
            print("Balance:", accounts[username]["balance"])

        elif choice == "2":
            amount = float(input("Amount to deposit: "))
            accounts[username]["balance"] += amount
            accounts[username]["last_transaction"] = f"Deposited {amount}"
            print("Added", amount)

        elif choice == "3":
            amount = float(input("Amount to withdraw: "))
            if amount > accounts[username]["balance"]:
                print("Not enough balance")
            else:
                accounts[username]["balance"] -= amount
                accounts[username]["last_transaction"] = f"Withdrew {amount}"
                print("Withdrawn", amount)

        elif choice == "4":
            receiver = input("Send to username: ").strip()
            if receiver not in accounts:
                print("No such user")
                continue
            amount = float(input("Amount: "))
            if amount > accounts[username]["balance"]:
                print("Not enough balance")
            else:
                accounts[username]["balance"] -= amount
                accounts[receiver]["balance"] += amount
                print("Sent", amount, "to", receiver)

        elif choice == "5":
            print("Logging out...")
            break

        else:
            print("Invalid option")


while True:
    print("\n1) Register  2) Login  3) Exit")
    c = input("Choice: ")
    if c == "1":
        register()
    elif c == "2":
        login()
    elif c == "3":
        break
    else:
        print("Invalid")