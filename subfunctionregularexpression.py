import re

data=input("Enter the data =")

old_data=input("Enter the old data =")

new_data=input("Enter the new data =")

new_string=re.sub(old_data,new_data,data)

print(new_string)
