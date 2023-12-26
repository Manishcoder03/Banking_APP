from random import randint


class Bank:
    def __init__(self) -> None:
        self.account = randint(100000, 999999)
        self.full_name = input("Enter name = ")
        self.phone_number = int(input("Enter phone number = "))
        self.balance = 0

    def show_info(self):
        print(f"Accout number = {self.account}")
        print(f"Full name = {self.full_name}")
        print(f"Balance = {self.balance}\n")

    def show_balance(self) -> None:
        print(f"Current balance = {self.balance}")

    def withdraw(self) -> None:
        amount = int(input("Enter amount to withdraw = "))
        if amount > self.balance:
            print("Insufficient balance")
        else:
            # self.balance = self.balance - amount
            self.balance -= amount

    def deposit(self) -> None:
        amount = int(input("Enter amount to deposit = "))
        self.balance = self.balance + amount


banks = []
while True:
    print("1. Create account")
    print("2. Show all bank details")
    print("3. Deposit amount")
    print("4. Withdraw amount")
    print("5. Exit")
    choice = int(input("Enter choice = "))
    if choice == 1:
        obj = Bank()
        banks.append(obj)
        print(banks)
    elif choice == 2:
        if len(banks) == 0:
            print("No accounts have been created yet")
        else:
            for account in banks:
                account.show_info()
    elif choice == 3:
        if len(banks) == 0:
            print("No accounts have been created yet")
        else:
            acc_no = int(input("Enter account number to deposit = "))
            for obj in banks:
                if obj.account == acc_no:
                    obj.deposit()
                    break
    elif choice == 4:
        pass  # Logic to withdraw
    elif choice == 5:
        break
    else:
        print("Invalid Choice")
