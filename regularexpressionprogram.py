import re
data=input("enter the data =")
search=input("what do you want to search =")
pattern=re.compile(search)
match=pattern.finditer(data)
count=0
for i in match:
    count+=1
    print(i.start(),"...",i.end(),"....",i.group())
print(search,"is existed for",count,"times")
