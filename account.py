lass BankAccount:
  bank="Equity"
  def __init__(self,first_name,last_name):
    self.first_name=first_name
    self.last_name=last_name
    self.balance=0
    
  def account_name(self):
    name="{} account for {} {}".format(self.bank,self.first_name,self.last_name)
    return name
  
  def get_balance(self):
    return "The balance for {} is {}. ". format(self.account_name(),self.balance) 
  
  def deposit(self,amount):
    if amount > 0:
     self.balance += amount
     print("You have deposited {} to your account".format(amount))
    else:
      print("you can not deposit {} amount")
  

  def withdraw(self,amount):
    if amount > 0:
     self.balance -= amount
     print("You have withdrawn {} from your account".format(amount))
    else:
      print("Kindly,you cannot withdraw {} amount")
  
      
    
acc1=BankAccount("Grace","Kimani")
acc2=BankAccount("Pesh","Njeri")
print (acc1.account_name())
print (acc2.account_name())
acc1.deposit(500)
acc2.deposit(79)
acc1.deposit(150)
acc2.deposit(209)
acc2.deposit(50)
acc1.deposit(300)

acc1.withdraw(500)
acc2.withdraw(150)
acc1.withdraw(200)
acc2.withdraw(90)
acc1.withdraw(70)
acc2.withdraw(170)


print(acc2.get_balance())
print(acc1.get_balance())
print(acc1.account_name())
print (acc2.account_name())
