n=input()
m={}
for i in range(1,n+1):
    m[((str)(i))]=1
res=True
b=set()
emp =raw_input().split()
for i in range(len(emp)):
    if emp[i]=="0":
        break
    elif i>0:
        b.add(emp[i])
emp =raw_input().split()
for i in range(len(emp)):
    if emp[i]=="0":
        break
    elif i>0:
        b.add(emp[i])
if len(b)==n:
    print "I become the guy."
else:
    print "Oh, my keyboard!"