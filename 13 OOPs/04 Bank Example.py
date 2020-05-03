import sys


class Customer:
    """Customer class for customer related operations od bank"""

    bankName = "Dev Bank"

    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def deposit(self, amnt):
        self.balance = self.balance + amnt
        print('After deposit, your balance is:', self.balance)

    def withdraw(self, amnt):
        if amnt > self.balance:
            print("Insufficient Balance, Can't perform this operation\nbalance is:", self.balance)
            sys.exit()
        self.balance = self.balance - amnt
        print("After withdraw, your balance is:", self.balance)


print("Welcome in", Customer.bankName)
name = input('Enter your name: ')
c = Customer(name)
while True:
    print()
    print("d to Deposit || w to withdraw || e to exit")
    response = input("Choose your operation: ")

    if response == "d" or response == "D":
        amnt = float(input('Enter amount to deposit: '))
        c.deposit(amnt)

    elif response.lower() == "w":       # First change response to lowercase then compare it with 'w'
        amnt = float(input('Enter amount to withdraw: '))
        c.withdraw(amnt)

    elif response == "e" or response == "E":
        print('Thanks for using our service')
        break
    else:
        print('Please Enter a valid key!!!')





