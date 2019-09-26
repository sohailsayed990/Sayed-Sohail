import re
count=0
pattern=re.compile("TCS")
match=pattern.finditer("TCS stands for tata consultancy services.TCS earns billlions of dollars on multinational projects")
for i in match:
    count+=1
print("TCS is existed for ",count,"times")
