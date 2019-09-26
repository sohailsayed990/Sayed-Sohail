f1=open("sohail1.txt","r")
f2=open("sohail2.txt","w")

data=f1.read()
f2.write(data)
print("success")
f1.close()
