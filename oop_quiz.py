# i.
class BankAccount:

    def __init__(self,account_number,balance,owner,type) -> None:
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        self.type = type

    def __str__(self) -> str:
        return 'the {} account is a {} type of account, is owned by {} and has a balance of {} '.format(self.account_number,self.type,self.owner,self.balance)
# ii.
class Bank:
    
    def __init__(self,name):
        self.name = name
        self.accounts = []


# add Bankaccount object to bank object and customer object

    def add_bankAccounts(self,BankAccount):
        self.accounts.append(BankAccount)
# print the bank object
    def __str__(self):
        return 'the {} bank has {} accounts '.format(self.name,self.accounts)

# iii.
# inheritance 
class Customer(Bank):

    def __init__(self,name):
        self.name = name
        self.accounts = []
    def __str__(self):
        return 'mr//mrs {} owns  {} accounts '.format(self.name,self.accounts)

# iv.
class Transactions:
    def __init__(self,amount,type):
        self.amount = amount
        self.type = type

    def add_account(self,BankAccount):
        self.add_account = BankAccount

# adding 2 objects
    def add_objects(self,other):
        return self + other

# new bank object

def create_bank(bank_name,account_list,bank_obj):
    bank_obj = Bank(bank_name)
    for account in account_list:
        bank_obj.add_bankAccounts(account)
    return bank_obj

# new customer object

def create_customer(customer_name,account_list,cust_obj):
    cust_obj = Bank(customer_name)
    for account in account_list:
        cust_obj.add_bankAccounts(account)

# new bankAccount object

def create_BankAccount(account_number,balance,owner,type,bankAcc_obj):
    bankAcc_obj = BankAccount(account_number,balance,owner,type)

# create transaction object

def create_Transaction(amount,type,account,trans_obj,bankAcc_obj):
    trans_obj = Transactions(amount,type)
    trans_obj.add_account(create_BankAccount)

