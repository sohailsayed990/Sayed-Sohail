username=['sohail@786']
password=['******']
u=input("\t\t\t\t\tUSERNAME :")
p=input("\t\t\t\t\tPASSWORD :")
if u in username and p in password:
	print("\t\t\t\t\tWelcome Mr.",u)
else:
	print("Wrong username or password")
	quit()
	
print("")
print("*******************************************************************")
print("\t\tWELCOME TO ONLINE SBI APPLICATION")

print("*******************************************************************")
print("")

print("1.Deposit")
print("2.Withdraw")
print("3.Account Summary")
print("4.Cheque Deposit")
print("5.LogOut")
print("")

print("*******************************************************************")


balance=500000
ans='yes'
while ans=='yes':			
	choice=int(input("Please Enter Your Choice ="))
	if choice==1:
		dep=int(input("Enter Your Deposit amount ="))
		balance+=dep
		print("After deposit your Main Balance is :",balance)
		print("")
		print("*******************************************************************")
	elif choice==2:
		withdraw=int(input("Enter withdraw amount ="))
		if withdraw<=balance:
			balance-=withdraw
			print("After withdraw your balance is",balance)
			print("")
			print("*******************************************************************")
		else:
			print("INSUFFICIANT FUND!!")
			print("")
			print("*******************************************************************")
	elif choice==3:
		print("You Main Balance is :",balance)
		print("")
		print("*******************************************************************")
	elif choice==4:
		cheqno=input("Enter Your Cheque Number =")
		cheqamt=int(input("Enter Your Cheque Amount ="))
		balance+=cheqamt
		print("After Adding Cheque Amount Your Main Balance is:",balance)
		print("")
		print("*******************************************************************")
	elif choice==5:
		print(u,"You are Log Out Successfully!!")
		print("")
		print("*******************************************************************")
		
		quit()
	else:
		print("Oops !! You Enter a wrong choice !!")
		print("")
		print("*******************************************************************")
	ans=input("Do you want to enter one more choice then type Yes/No :")
