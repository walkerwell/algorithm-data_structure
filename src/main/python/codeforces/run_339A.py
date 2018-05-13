a=map(int,raw_input().split("+"))
a.sort()
res=""
for i in range(len(a)):
    if(i==len(a)-1):
        res+=(str)(a[i])
    else:
        res+=(str)(a[i])+"+"
print res