import re
search=input("what do you want to search =")
match=re.fullmatch(search,"practice makes man perfect.")

if match!=None:
    print("Match is found")
else:
    print("Match is not found")
