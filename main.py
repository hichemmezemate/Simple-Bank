from datetime import datetime

class bank:

    def __init__(self, initial_balance = 0.00):
        self.balance = initial_balance

    def transactions(self, transaction_line):
        time_now = datetime.now()
        time_now_now = time_now.strftime("%D/%m/%Y, %H:%M:%S")
        with open("transactions.txt", "a") as file:
            file.write(f"{transaction_line} \t\t\t {time_now_now}\t Balance: {self.balance}\n")

    def show_balance(self):
        print(f"The balance is {self.balance}\n")

    def show_transactions(self):
        with open("transactions.txt", "r") as file:
            print("Your transactions:")
            return file.read()

    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance + amount
            self.transactions(f"Deposit {amount}")

    def withdrawal(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance - amount
            self.transactions(f"Withdrew {amount}")
            print(f"You withdrawed {amount}\n")

    

bank_user = bank(100.00)

while True:
    try:
        action = input("Choose an action: (1 for withdrawal, 2 for deposit, 3 to show transactions)  ")
    except KeyboardInterrupt:
        print("\n.....Leaving.....\n")
        break

    if action in ["1", "2", "3"]:
        if action == "1":
            amount = input("How much do you want to withdraw ")
            bank_user.withdrawal(amount)
        elif action == "2":
            amount = input("How much do you want to deposit? ")
            bank_user.deposit(amount)
        else:
            transactions = bank_user.show_transactions()
            print(transactions)
    else:
        print("Please choose a valid action!")
        