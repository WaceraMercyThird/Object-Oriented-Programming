

class Account:
   
    
    def __init__(self,name,accountnumber,pin):
        self.balance=0
        self. name= name
        self. accountnumber= accountnumber
        self.pin=pin
        self.deposits=[]
        self.withdraws=[]

     # class Method
    def deposit(self,deposit):

        if deposit <= 0:
            return f"Deposit amount should be more that 0"
        else:
            self.balance+= deposit
            self.deposits.append(deposit)
            return f"you have deposited {deposit}Kshs, and this is your new balance {self.balance}Kshs" 
        
    def withdraw(self,withdraw):
        if withdraw>self.balance:
           return f"your balance is {self.balance}Kshs, you cannot withdraw {withdraw}Kshs"
        elif withdraw<0:
           return f"your amount should be more that zero"
        else:
            self.balance-= withdraw
            self.withdraws.append(self.balance)
            return f"you have withdraw {withdraw}Kshs, and this is your new balance {self.balance}Kshs" 
          
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

    





 


    

        

   
