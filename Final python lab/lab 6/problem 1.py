class BankAccount:

    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Current Balance:", self.balance)



account = BankAccount(
    "AC1001",
    5000,
    "15-09-2026",
    "Atif"
)

print("Account Number:", account.account_number)
print("Customer Name:", account.customer_name)
print("Date of Opening:", account.date_of_opening)

account.check_balance()

account.deposit(2000)
account.check_balance()

account.withdraw(1500)
account.check_balance()

account.withdraw(10000)