import re

pattern=re.compile("\s")
match=pattern.finditer(" 7abc@kl1980dc. ")
for i in match:
    
    
    print(i.start(),"...",i.group())
    
