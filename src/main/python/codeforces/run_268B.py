n=input()
it=0
res=0
while(n>1):
    res+=((n-1)*it)+n
    it+=1
    n-=1
print res+1