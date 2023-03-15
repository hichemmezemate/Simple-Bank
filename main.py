class bank:

    def __init__(self, initial_balance = 0.00):
        self.balance = initial_balance

    def transactions(self, transaction_line):
            with open("transactions.txt", "a") as file:
                file.write(f"{transaction_line} \t\t\t Balance: {self.balance}\n")

    def show_balance(self):
        print("The balance is", self.balance)

    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance + amount
            self.transactions(f"Deposit {amount}")



    def withdraw(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance - amount
            self.transactions(f"Withdrew {amount}")

    

banque = bank(100.00)
banque.show_balance()
banque.withdraw(25.25)
banque.show_balance()
        