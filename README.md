## Welcome!
Thank you for checking my repo.

To do the following work you need to have an understanding to the basics of python.
How to create a class and add attribute respectively.
Willing to think logically about how money transaction work, all in all you can do it


## Class Methods
Do the following to reach the target of each and every transaction step.
Ensure deposit and withdraws are functioning as expected in the finance.
**I may be wrong but avoid looking my solution to the problem before attempting by yourself first**

## Challenge
Kindly read, understand and follow the instruction to get the expected outcome.
1. Add these methods to class student - full_name, year_of_birth, initials. Create two instances and verify the work as expected
2. Add these methods to class Account - deposit, withdraw. Create two instances of account and verify they work as expected.
3. Add a new attribute to the class Account called deposits which by default is an empty list.
4. Add another attribute to the class Account called withdrawals which by default is an empty list.
5. Modify the deposit method to append each successful deposit to self.deposits
6. Modify the withdrawal method to append each successful withdrawal to self.withdrawals
7. Add a new method called deposits_statement which prints each deposit in a new line
8. Add a new method called withdrawals_statement which prints each withdrawal in a new line
9. Modify the withdrawal method to include a transaction fee of 100 per transaction.
10. Add a method to show the current balance
11. Update the withdrawal method to store each withdrawal transaction as a dictionary like like this 
{
   "date": datetime object,
   "amount": amount,
   "narration": deposit or withdrawal
}

12. Update the deposit method to store each deposit transaction as a dictionary like this 
{
   "date": datetime object,
   "amount": amount,
   "narration": deposit or withdrawal
}

13. Add a new method  full_statement which combines both deposits and withdrawals into one list ordered by date and using a for loop prints each transaction in a new line like this
16/06/22 —----- Deposit —---- 1000

14. Add a new attribute loan_balance which is zero by default.

15. Add a borrow method which allows a customer to borrow if they meet these conditions:
- Customer has made at least 10 deposits.
- Loan amount requested must be more than 100
- A customer qualifies for a loan amount that is less than  or equal to 1/3 of their total sum of deposit history
- Customer account has no has no balance
- Customer has no outstanding loan
- The loan attracts  an interest of 3%.

16. Add a loan repayment method with these conditions
- A customer can repay a loan to reduce the current loan balance
- Overpayment of a loan increases a customers current deposit

17. Add a new method transfer which accepts two attributes (amount and instance of another account). If the amount is less than the current instances balance, the method transfers the requested amount from the current account to the passed account. The transfer is accomplished by reducing the current account balance and depositing the requested amount to the passed account.



Your user should be able to:

- Add deposit and recieve a message desplaying the balance in the account.
- Withdraw money from there account and return a message showing how much has been deductin and the new balance in the bank account.
- See each and every deposit the user deposited.
- See withdraw that was taken from the bank.
- See the transaction fee that deduction from their withdrawal.
- Recieve a message that display the current balance remaining in the account.
