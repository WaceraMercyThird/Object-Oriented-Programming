
# Add these methods to class Account - deposit, withdraw. Create two instances of account and verify they work as expected.


class Account:
    
    def __init__(self,name,accountnumber,pin):
        self.balance=0
        self. name= name
        self. accountnumber= accountnumber

        self.pin=pin

     # class Method
    def deposit(self,deposit):
        self.balance+= deposit
        if deposit <= 0:
            return f"Deposit amount should be more that 0"
        else:
            return f"you have deposited {deposit}, and this is your new balance {self.balance}" 
        

    def withdraw(self,withdraw):
       if withdraw>self.balance:
           return f"your balance is {self.balance}, you cannot withdraw {withdraw}"
       elif withdraw<0:
           return f"your amount should be more that zero"
       else:
           self.balance-= withdraw
           return f"you have deposited {withdraw}, and this is your new balance {self.balance}" 
        
    


    

        

   