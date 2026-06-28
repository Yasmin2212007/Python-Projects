print("*" *50)
print("Welcome To My  Instant Discount System")
print("*" *50)

Name=input("Enter Your Name: ")
price=int(input("Enter The Price Of your  purchases : "))


if price < 0:
    print("Invalid Price")

elif price < 100 :
    print(f"Sorry {Name},No Discount For You ")
    print(f"You Should Pay ${price}")

elif price < 500 :
    print(f"{Name} You have a 10% discount")
    new_price=price*0.9
    print(f"You Should Pay ${new_price}")

else :
    print(f"{Name} You have a 20% discount")
    new_price = price * 0.8
    print(f"You Should Pay ${new_price}")