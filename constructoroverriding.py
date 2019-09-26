class bank:
    def __init__(self):
        self.balance=0
        self.deposit=input("enter deposit amount=")
        self.balance+=self.bdeposit
        print("after deposit your main balance is :",self.balance)
class sbi(bank):
    def __init__(self):
        self.balance=0
        deposit=int(input("enter deposit amount="))
        self.balance+=deposit
        print("after deposit your main balance is :",self.balance)
        self.intrest=self.balance*0.04
        self.balance+=self.intrest
        print("after adding intres your balance is :",self.balance)
        
s1=sbi()
