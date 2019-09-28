import re

code="<html><head><titile>mobiles information </title></head><body><ul><li>samsung</li><li>sony</li><li>redmi</li><li>lava</li></ul></body></html>"

regex=re.compile("<li>.*</li>")

match=re.findall(regex,code)

print(match)
