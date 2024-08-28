#just doing basic writng/calling functions
import os, time

balance = 1500

def showBalance():
    print("Your balance is: $", balance)

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: $"))
    balance += amount
    print("Your new balance is: $", balance)
    time.sleep(2.4)
    os.system("clear")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: $"))
    if balance >= amount:
        balance -= amount
        print("Your new balance is: $", balance)
        time.sleep(2.4)
        os.system("clear")
    else:
        print("Insufficient balance.")
        time.sleep(2)
        os.system("clear")

while True:
    print("Welcome to the ATM!")
    print()
    time.sleep(1)
    os.system("clear")
    choice = input("What do you want to do:\n1: Deposit\n2: Withdraw\n3: Check Balance\n4: Quit\n")
    if choice == "1":
        deposit()
    elif choice == "2":
        withdraw()
    elif choice == "3":
        showBalance()
    elif choice == "4":
        print("Thank you for using the ATM!")
        break
