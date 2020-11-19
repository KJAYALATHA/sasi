n=input("enter the value:")
p=len(n)
m=''
for i in range(0,p,2):
    if n[i].isalpha() and n[i+1].isnumeric():
        a=n[i]
        b=int(n[i+1])
        m=m+(a*b)
    else:
         m="INVALID INPUT"
         break
print(m)
