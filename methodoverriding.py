class bank:
    balance=0
    
    def m1(self):
        print("method m1 executed")
    def dep(self):
        
        
        self.deposit=int(input("enter deposit amount="))
        bank.balance+=self.deposit
        print("after deposit your main balance is :",bank.balance)
        
class sbi(bank):
    def dep(self):
        deposit=int(input("enter deposit amount="))
        bank.balance+=deposit
        print("after deposit your main balance is :",bank.balance)
        self.intrest=bank.balance*0.04
        bank.balance+=self.intrest
        print("after adding intres your balance is :",bank.balance)
        
s1=sbi()
s1.dep()
