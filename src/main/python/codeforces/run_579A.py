n=input()
res=0
while(True):
    res+=n&1
    n=n>>1
    if n==0:
        break
print res