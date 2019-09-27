ans='yes'
while ans=='yes':
	try:
		num=int(input("Enter An Number ="))

		orignal=num
		rem=rev=0
		while num!=0:
			rem=num%10
			rev=rev*10+rem
			num=num//10
		print("Reverse Number is :",rev)
		if orignal==rev:
			print(orignal,"Is An Palindrom Number")
		else:
			print(orignal,"Is Not An Palindrom Number")
	except ValueError:
		print("Enter only Numeric Value")
	ans=input("Do you want to enter one more value type yes/No :")
