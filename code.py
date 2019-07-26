import re

f=open("tele.txt","r")
r=f.read()
print("Telephone Directory")
print("--------------------\n\n")
c3=re.findall('\d{3}',r)
c4=re.findall('\d{4}',r)
print ("3 Digit Code ")
print("--------------------\n\n")
print(c3)
print ("Count of the Codes: ",len(c3),"\n")
print ("4 Digit Code ")
print("--------------------\n\n")
print(c4)
print ("Count of the Codes: ",len(c4))

f.close()
