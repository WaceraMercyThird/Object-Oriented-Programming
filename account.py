
# Add these methods to class Account - deposit, withdraw. Create two instances of account and verify they work as expected.


class Account:
    
    def __init__(self,name,accountname,balance,pin):
        self. name= name
        self. accountname= accountname
        self.balance=balance
        self.pin=pin

     # class Method
    def deposit(self,deposit):
        self.balance+= deposit


        return f"{self.balance}"
        

    def withdraw(self,withdraw):
       self.balance-= withdrawa
       return f"{self.balance}"

        

   