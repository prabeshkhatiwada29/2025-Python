# encapsulation
# Wrapping data and function into a single(object)
# data and function

class Account:
     def __init__(self, account_number, balance):
          self.balance= balance
          self.account_number = account_number

# debit method

     def debit(self, amount):
          self.balance-=amount
          print(f"Debit: ${amount}")
          print(f"Balance: ${self.balance}")


     def credit(self, amount):
          self.balance+=amount
          print(f"Debit: ${amount}")
          print(f"Balance: ${self.balance}")
    
     def get_balance(self):
          return self.balance




acc1=Account(1000,3333)
acc1.debit(1000)
acc1.credit(500)
acc1.debit(500)
acc1.credit(500)




