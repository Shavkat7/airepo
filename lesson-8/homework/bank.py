account_number_start = 100_000


class Account:
    account_number = 0
    name = ''
    balance = 0
    
    def __init__(self, name, balance=0):
        self.balance = balance
        self.name = name
        global account_number_start
        self.account_number = account_number_start + 1
        account_number_start += 1

    def __str__(self):
        return f"Account number: {self.account_number}, name: {self.name}, balance: {self.balance}"



class Bank:

    accounts = {}

    def __init__(self):
        self.load_from_file()


    def create_account(self, name, initial_deposit):
        
        #Create a new account, push it to the list of accounts and save to file
        
        account = Account(name, initial_deposit)
        self.accounts[account.account_number] = [account.name, account.balance]
        self.save_to_file()


    def view_account(self, account_number):
        print(f"The account number: {account_number}")
        self.load_from_file()
        account_info = self.accounts.get(account_number, None)
        if account_info:
            return f"Name: {account_info[0]}, balance: {account_info[1]}"
        else:
            return "Account not found"
        


    def deposit(self, account_number, amount):
        with open("bank_accounts_list.txt", "r") as file:
            lines = file.readlines()

        with open("bank_accounts_list.txt", "w") as file:
            for line in lines:
                if account_number == int(line.split(",")[0]):
                    file.write(f"{line.split(",")[0]},{line.split(",")[1]},{int(line.split(",")[2])+amount}\n")
                else:
                    file.write(line)


    def withdraw(account_number, amount):
        with open("bank_accounts_list.txt", "r") as file:
            lines = file.readlines()

        with open("bank_accounts_list.txt", "w") as file:
            for line in lines:
                if account_number == int(line.split(",")[0]):
                    if int(line.split(",")[2]) < amount:
                        return "Insufficient balance"
                    file.write(f"{line.split(",")[0]},{line.split(",")[1]},{int(line.split(",")[2])-amount}\n")
                else:
                    file.write(line)

    def save_to_file(self):
        with open('bank_accounts_list.txt', 'w') as file:
            for account_num, account_info in self.accounts.items():
                file.write(f"{account_num},{account_info[0]},{account_info[1]}\n")

    def load_from_file(self):
        with open("bank_accounts_list.txt", "r") as file:
            for line in file:
                if not line.isspace():
                    self.accounts[int(line.split(',')[0])] = [line.split(',')[1], line.split(",")[2]]

        

bank = Bank()
# bank.create_account("Sohib", 4300001)
# bank.create_account("Shoxa", 9108988)
print(bank.view_account(100001))
bank.deposit(100001, 100)
print(bank.view_account(100001))
# print(bank.deposit(100002, 99))