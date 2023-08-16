"""
Розробіть клас BankAccount для представлення банківського рахунку.
Додайте методи для зняття та поповнення коштів на рахунку.
Використовуйте магічний метод __str__ для виведення інформації про рахунок.
"""


class BankAccount:

    def __init__(self,account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def add_cash(self, amount):
        self.balance += int(amount)

    def withdrawal_cash(self, amount):
        self.balance -= int(amount)

    def __str__(self):
        return f"Hello, {self.owner_name}, your account {self.account_number} balance is: {self.balance}$"


account1 = BankAccount("123456", "Tom Hanks", 3589)

account1.add_cash(1000)
account1.withdrawal_cash(3000)

print(account1)
