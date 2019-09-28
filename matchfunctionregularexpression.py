import re
search=input("what do you want to search =")
match=re.match(search,"India is my country.")
if match!=None:
    print("Match is found")
else:
    print("Match is not found")
