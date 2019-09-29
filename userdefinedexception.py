class nofunds(Exception):
	def __init__(self,message):
		self.exception_message=message
balance=8000
withdraw_amt=int(input("Enter Withdraw Amount ="))
if withdraw_amt<=balance:
	balance-=withdraw_amt
	print("After Withdaw Amount =",balance)
else:
	raise nofunds("insufficient funds")