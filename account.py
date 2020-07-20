class BankAccount:
  
  def __init__(self,first_name,last_name,bank,phone_no):
    self.first_name=first_name
    self.last_name=last_name
    self.bank=bank
    self.phone_no=phone_no
    self.balance=0
    self.withdraw_statement = []
        self.deposit_statement = []
        self.loan_balance = 0


  def account_name(self):
    name="{} account for {} {}".format(self.bank,self.first_name,self.last_name)
    return name
  
  def get_balance(self):
    return "The balance for {} is {}. ". format(self.account_name(),self.balance) 
  
  def deposit(self,amount):
    if amount <= 0:
       print("you cannot deposit zero or negative")
    else:
        self.balance +=amount
        print("you have deposited {} to {}".format(amount,self.account_name()))
  def withdraw(self,amount):
    if amount <=0:
     print("You cannot withdraw  zero or negative")
    elif amount>self.balance:
        print("you have insufficient balance")
    else:
         self.balance -=amount
         print("you have withdrawn {} from {}".format(amount,self.account_name()))
  
      
    def lend_loan(self, loan):
      if loan <= 0:
        print("Invalid request")
        
      else: 
        self.loan_balance += loan
        print("{} you have borrowed {}".format(self.account_name(), loan))
      
    def pay_loan(self, loan):
      if loan <= 0:
        print("Invalid amount to reduce your loan")
      else:
        self.loan_balance -= loan
        print(" You have repaid {}".format(loan))
      
    def deposit_statement(self, amount):
      self.deposit(self, amount)
      
      return self.deposit_summary.append(amount)
      
      
       
      
    
