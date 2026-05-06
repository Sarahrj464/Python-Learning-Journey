class Account:
  def __init__(self,balance,account_no):
    self.balance=balance
    self.account_no=account_no
  
  def debit(self,amount):
    self.balance-=amount
    print("Rs.",amount,"was debited")
    print("total balance:",self.getbalance())
    
  def credit(self,amount):
    self.balance+=amount
    print("Rs.",amount,"was credited")
    print("total balance:",self.getbalance())
    
  def getbalance(self):
    return self.balance
    
a1=Account(10000,12345678) 
a1.debit(1000)
a1.credit(500)
a1.credit(2000)
a1.debit(1000)
    
    