class BankAccount:
    def __init__(self,account_owner,account_number,initial_balance):
        self.account_owner = account_owner
        self.account_number = account_number
        self.balance = initial_balance
    
    def make_deposit(self,amount):
        self.balance += amount

    def make_withdraw(self,amount):
        if self.balance - amount >= 0:
            self.balance -= amount    
        else:
            print("Insufficient funds")
    def __bool__(self):
        return self.balance > 0

my_account = BankAccount("Nora Nav","356-2456--2455",45045.23)

print(my_account.balance)
print(bool(my_account))
my_account.balance = 0 
print(my_account.balance)
print(bool(my_account))