def deposit():
	acc_no=int(input("Enter Your Account Numer ="))
	acc_type=input("Enter Your Account Type =")
	deposit_amount=int(input("Enter Deposit Amount ="))
	balance=500000
	
	balance+=deposit_amount
	
	return balance