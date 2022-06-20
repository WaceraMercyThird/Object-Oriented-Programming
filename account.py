from datetime import datetime


class Account:
   
    
    def __init__(self,name,accountnumber,pin):
        self.balance=0
        self. name= name
        self. accountnumber= accountnumber
        self.pin=pin
        self.deposits=[]
        self.withdraws=[]
        self.withdrawal_transaction=[]
        self.time= datetime.now().strftime("%X")
        self.loan_balance=0

     # class Method
    def deposit(self,amount):

        if amount <= 0:
            return f"Deposit amount should be more that 0"
        else:
            self.balance+= amount
            transaction= {
                "date": self.time,
                "amount": amount,
                "narration": "You have deposited"
                }
            self.withdrawal_transaction.append(transaction)
            self.deposits.append(amount)
            return f"you have deposited {amount}Kshs, and this is your new balance {self.balance}Kshs" 
        
    def withdraw(self,amount):
        if amount>self.balance:
           return f"your balance is {self.balance}Kshs, you cannot withdraw {amount}Kshs"
        elif amount<0:
           return f"your amount should be more that zero"
        else:
            self.balance-= amount
            transaction= {
                "date": self.time,
                "amount": amount,
                "narration": "You have withdrawn"
                }
            self.withdrawal_transaction.append(transaction)
            self.withdraws.append(self.balance)
            return f"you have withdraw {amount}Kshs, and this is your new balance {self.balance}Kshs" 
          
    def deposit_statement(self):
        for k in self.deposits:
            print(f"{k}Kshs") 

    def withdraw_statement(self):
        for n in self.withdraws:
            print(f"{n}Kshs") 

    def withdrawal(self):
        for n in self.withdraws:
            x=n-100
            print(f"Transaction fee of {x}Ksh was deduction 100Kshs.") 
        
    def current_balance(self):
        bal=self.balance
        print(f" you new balnce is {bal}Kshs")

    def statement(self):
        for transaction in self.withdrawal_transaction:
            date = transaction["date"]
            amount = transaction["amount"]
            narration = transaction["narration"]
            print(f"{date}: {narration} {amount}Kshs")

    def borrow (self,amount):

        count = sum (self.deposits)
        limit = count
        interest = amount*0.03
        if amount<=100:
            return "Loan must be more than 100"
        elif self.loan_balance>0:
            return "Loan denied, kindly repay your current loan of {self.loan}"
        elif len(self.deposits)<10:
            return f"you deposits must be at least more than 10"
        elif amount>=limit:
            return f"You have reached your limit, your loan of {amount}Kshs is denied" 
        elif amount>=self.balance:
            return f"Dear customer you can't borrow that money is lower than a limit of"
        else:
            self.loan_balance>=amount
            self.loan_balance+=interest
            transaction= {
                "date": self.time,
                "amount": amount,
                "narration": "You have withdrawn"
                }
            self.withdrawal_transaction.append(transaction)
            return f"Hello {self.name} your loan of {amount} has been approved and your interest is {interest} you will pay back {self.loan_balance}"

    def repay(self,amount):
        if amount<8: 
            return f"Dear customer your payment is too low"
        elif amount<=self.loan_balance:
            paid= self.loan_balance - amount
            return f"Dear customer you have paid {amount} and your loan balance is {paid}"
        else:
            payment = amount - self.loan_balance
            self.balance+=payment
            transaction= {
                "date": self.time,
                "amount": amount,
                "narration": "You have withdrawn"
                }
            self.withdrawal_transaction.append(transaction)
            return f"Dear customer {self.name} you have fully paid your loan and the overpay of {payment} is added on your account, your new balance is {self.balance}"
    def transfer(self, account_instance,amount):
        total = amount + self.withdrawal
        if amount<0:
            return f"Dear customer {self.name} your amount is too low"
        elif total>self.balance:
            return f"Your balance is {self.balance} and you need atleast {total}"
        else:
            self.balance-=total
            return f"you have sent {amount} to {account_instance} your current balance is {self.balance}"

