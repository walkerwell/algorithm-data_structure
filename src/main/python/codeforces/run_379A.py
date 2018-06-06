a,b=map(int,raw_input().split())
res=a
left=0
while(True):
    n=(a+left)/b
    if(n>0):
        left=(a+left)%b
        a=n
        res+=a
    else:
        break
print res