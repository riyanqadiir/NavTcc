# Q6: Secure BankAccount Class

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.__balance

# Demo
acc = BankAccount()
acc.deposit(1000)
print(acc.get_balance())
acc.withdraw(300)
print(acc.get_balance())
acc.withdraw(1000)  # Should show insufficient funds
