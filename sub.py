class ATM:
    def __init__(self, password,balance):
        self.password = password
        self.balance=balance
        self.withdrawl_history = []
        self.deposit_history=[]

    def authenticate(self, pin):
        global choice
        self.pin = pin
        if self.pin == self.password:
            while choice!=5:
                  choice = int(input('''******main menu******
                                  1.Transaction History
                                  2.withdrawl
                                  3.deposit
                                  4.transfer
                                  5.Quit
                                Enter your choice'''))
                  if choice == 1:
                      account.transaction_history()
                  elif choice == 2:
                      account.process_withdrawl()
                  elif choice == 3:
                      account.deposit_money()
                  elif choice==4:
                      account.transfer(source_user)
                  else:
                      exit(0)
            exit(0)
        else:
            print("authentication failed,try again")
    def process_withdrawl(self):
        amount = int(input("enter the amount for withdrawl"))
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(amount, " debited from account")
            print("Total balance available is ", self.balance)
        self.withdrawl_history.append(amount)

    def deposit_money(self):
        amount = int(input("enter the amount for deposit"))
        self.balance = self.balance + amount
        print(amount, " credited from account")
        print("Total balance available is", self.balance)
        self.deposit_history.append(amount)
    def transaction_history(self):
        print("withdraws:", self.withdrawl_history)
        print("Deposits:", self.deposit_history)
    def transfer(self, source_user):
        self.source_user = source_user
        destination_user = int(input("enter the id of destination_user"))
        amount = int(input("enter the amount to be transfered"))
        self.balance = self.balance - amount
        self.deposit_history.append(amount)
        print("Amount transfered succesfully ")
        print("Balance amount available is", self.balance)


print("Welcome to ICIC Bank\n\nInsert your card")
password = 1234
balance = 10000
choice=0
user_id = int(input("Enter the user id"))
pin = int(input("Enter your four digit pin"))
source_user=user_id
account=ATM(password,balance)
account.authenticate(pin)
