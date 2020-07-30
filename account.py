
class Account:
   

    def __init__(self, first_name, last_name, phone_no, bank):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_no = phone_no
        self.bank = bank
        self.balance = 0
        self.withdraw_summary = []
        self.deposit_summary = []
        self.loan_balance = 0

    def account_name(self):
        name = "{} account for {} {}".format(
            self.bank, self.first_name, self.last_name, self.phone_no, self.bank)
        return name

    def deposit(self, amount):
      
      if amount <= 0:
               
          print("You cannot deposit zero or negative")
      else:
            self.balance += amount
            print("You have deposited {} to {}".format(amount, self.account_name()))
            return 
            
            
          
    def withdraw(self, amount):
         
      if amount <= 0:
          print("You cannot withdraw zero or negative")
          
       
      elif amount > self.balance:
            print("You don't have enough balance")
      self.balance += amount
      time = datetime.now()
      get_time = time.strftime("%H:%M%p %d/%m/%Y")
      get_time = time.strftime("%H:%M%p , %d/%m/%Y")
      deposit = {
                "time": "time",
                "amount" : "amount"
            }
      print("Dear {} you have deposited {} at {}.Your current balance is {}".format(self.account_name(),amount,get_time,self.balance))
      print("Dear {} ,you have deposited {} at {}.Your current balance is {}".format(self.account_name(),amount,get_time,self.balance))

    def withdraw(self,amount):
        try:
@@ -53.6 +60.7 @@ def withdraw(self,amount):
        else:
            self.balance -= amount
            time = datetime.now()
            get_time = time.strftime("%H:%M%p  %d/%m/%Y")
            get_time = time.strftime("%H:%M%p ,  %d/%m/%Y")
            deposit = {
                "time": "time",
                "amount" : "amount"
@@ -83,24 +63,19 @@ def withdraw(self,amount):

    def get_balance(self):
        time = datetime.now()
        get_time = time.strftime("%H:%M%p  %d/%m/%Y")
        get_time = time.strftime("%H:%M%p ,  %d/%m/%Y")
        return "The balance for {} is {} at".format(self.account_name(), self.balance,get_time)

    def deposit_statements(self):
        for deposit in self.deposits:
            time = datetime.now()
            get_time = time.strftime("%H:%M%p  %d/%m/%Y")
            get_time = time.strftime("%H:%M%p  , %d/%m/%Y")
            print("{} at {}".format(deposit(),get_time))

    def withdrawal_statements(self):
        for withdraw in self.withdrawals:
            time = datetime.now()
            get_time = time.strftime("%H:%M%p  %d/%m/%Y")
            get_time = time.strftime("%H:%M%p , ++ %d/%m/%Y")
            print("{} at {}".format(withdraw(),get_time))
   def request_loan(self, amount):
     try:
       amount=10
       except TypeError!
       print("please enter the requested amount")
       return
      if amount<= 0:
        print("You cannot requet for loan of tht amount")
        
      else: 
        self.loan = amount
        print("You have been given loan of {}".format (amount)
      
    def repay_loan(self, amount):
      try:
        amount = 10
        except TypeError:
          print("Enter the repayment in figure")
      if amount<= 0:
        print("You cannot repay with that amount")
      elif self.loan == 0:
        print("You don't have loan at the moment")
        elif amount > self.loan:
          print("your loan is {}, please enter amount that is less or equal to the amount")
        else:
          self.loan=amount
          time=datetime.now()
          repayment = {
            "time":time,
            "amount":amount
          }
          self.loan-repayment.append(repayment)
        print(" You have repayed your loan with {}.your loan balance is{}".format(mount))
    
      def loan-repayment-statement(self):
        for repay6ment in self.loan-repayment
        time = repayment("time")
        amount = repayment ("amount")
        formatted-time = self.get-formatted time("time")
        statement = "you repaid {} on {}".format(amount,formatted-time)
        print(statement)
        #inherintance
class BankAccount(Account):
    def __init___(self,first_name,last_name):
            self.bank=bank
            super().__init__(first_name,last_name,phone_no)    

class MobileMoneyAccount(Account):
    def __init__(self,first_name,last_name,phone_no,service_provider):
            self.service_provider=service_provider
            self.airtime=[]
            super().__init__(first_name,last_name,phone_no)
    def buy_airtime(self,amount):
        try:
                 amount-1
        except TypeError:
            print("please enter amount in figures")
            return
        if amount>self.balance:
                 print("you dont have enough balance.your balance is {}".format(self.balance))
        else:
            self.balance-=amount
            time=datetime.now()
            airtime={
                "time":time
                "airtime":amount
            }
            self.airtime.append(airtime)
            print("you have bought airtime worth {} on {}".format(amount,self.get_formatted_time(time)))
    def paybills(self,amount):
        try: 
            amount-1
        except TypeError:
            print("please enter amount in figures")
            return
        if amount>self.balance:
            print("You have insufficient balance.Your balance is {}".format(self.balance))

        else:
            self.balance-=amount
            time=datetime.now()
            paybills={
                "time":time
                "paybills":amount
            }
            self.paybills.append(paybills)
            print("you have paid bills worth {}.your balance is {}".format(amount,self.get_formatted_time(time)))
    def send_money(self,amount):
        try:
            amount-1
        except TypeError:
            print("please enter amount in figures") 
            return
            if amount>self.balance:
                print("failed.insuffcient fundsin your account.your balance is {}".format(self.balance))
                else:
            self.balance-=amount
            time=datetime.now()
            money={
                "time":time
                "money":amount
            }
            self.money.append(money)
            print(" confirmed  you have sent {} .your balance is {}".format(amount,self.get_formatted_time(time)))
    def receive_money(self):
        time=datetime.now()
        money_received={
            "time":time
            return  "You have received {}.your balane is {}".format(self.get_formatted_time)
            
        }
        
    
























      
    
acc1 = BankAccount(" Grace", "Kimani", +254717468222, " Equity")
print(acc1.phone_no)
acc1.deposit(50000)
acc1.withdraw(15000)
acc1.withdraw(1200)
acc1.deposit(4000)
acc1.deposit(2400)
acc1.lend_loan(7000)
acc1.lend_loan(20000)
acc1.pay_loan(15000) 
print(acc1.loan_balance)

print(acc1.deposit_statement)



        
        
        
        
         
      
      
      
       
      
    
