#1.FUNCTION WITH PARAMETER WITHOUT RETURN VALUE
'''
class deposit:
	def deposit(self,acc_no,acc_type,deposit_amount):
		self.balance=500000
		self.balance+=deposit_amount
		print("After Deposit Main Balance is :",self.balance)

d1=deposit()
d1.deposit(1223,'saving',70000)'''

#2.FUNCTION WITH PARAMETER WITH RETURN VALUE
'''
def deposit(acc_no,acc_type,deposit_amount):
		balance=500000
		balance+=deposit_amount
		return balance'''
#3.FUNCTION WITHOUT PARAMETER WITH RETURN VALUE
'''
def deposit():
	acc_no=int(input("Enter account no ="))
	acc_type=input("Enter account Type=")
	deposit_amount=int(input("Enter Deposit Amount ="))
	
	balance=500000
	balance+=deposit_amount
	return balance'''

#4.FUNCTION WITHOUT PARAMETER WITHOUT RETURN VALUE
'''
def deposit():
	acc_no=int(input("Enter account no ="))
	acc_type=input("Enter account Type=")
	deposit_amount=int(input("Enter Deposit Amount ="))
	
	balance=500000
	balance+=deposit_amount
	print("After deposit balance is :",balance)
		'''


