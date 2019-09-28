import re
f1=open("html.txt","r")
regex=re.compile("<body>.*</body>")
match=re.findall(regex,f1)

print(match)
