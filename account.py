

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
            self.deposits.append(self.balance)
            return f"you have deposited {deposit}, and this is your new balance {self.balance}" 
        
    def withdraw(self,withdraw):
        if withdraw>self.balance:
           return f"your balance is {self.balance}, you cannot withdraw {withdraw}"
        elif withdraw<0:
           return f"your amount should be more that zero"
        else:
            self.balance-= withdraw
            self.withdraws.append(self.balance)
            return f"you have withdraw {withdraw}, and this is your new balance {self.balance}" 
          
    def deposit_statement(self):
        print(*self.deposits, sep="\n")

    def withdraw_statement(self):
        print(*self.withdraws, sep="\n")


 


    

        

   
