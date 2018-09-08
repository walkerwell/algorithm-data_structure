n=input()
res=0
cost=0
for _ in raw_input().split():
    a=(int)(_)
    if a>0:
        cost+=a
    else:
        if cost>0:
            cost-=1
        else:
            res+=1
print res