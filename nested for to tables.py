table=1
for i in range(1,11):
	print("table of",table)
	for mul in range(1,11):
		print(table,"*",mul,"=",table*mul)
		mul+=1
	print("")
	table+=1
