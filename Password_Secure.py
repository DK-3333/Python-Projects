#I secure my passowrd using Python
import string
import random

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation
s = []
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)


plen = int(input("Enter the length of the password : "))
b = input("Enter your desired password : ")
if len(b)==plen:
    pass
else:
    print("Enter the password of your desired length.")
    exit() 
a = random.sample(s,plen)
#print(a)
e = list(b)
c = list(b)
c[0] = a[0]
c[int(plen/2)]=a[int(plen/2)]
c[plen-1] = a[plen-1]
d = "".join(c[0:plen])
print(f'''Your secure password is {d}.Here {e[0]} is equals to {c[0]},
{e[int(plen/2)]} is equals to {c[int(plen/2)]},
{e[plen-1]} is equals to {c[(plen-1)]}.''')
