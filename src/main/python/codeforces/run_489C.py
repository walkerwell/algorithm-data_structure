n,m = [int(i) for i in input().split()]
def sum_(a):
    res=0
    for i in str(a):
        res+=int(i)
    return res
if sum_(10**(n-1)) > m:
    print(-1,-1)
    exit(0)
emp=10**n-1
max_= 0
while(True):
    if sum_(emp) == m:
        max_ = emp
        break
    emp-=1
emp=10**n-1
index=10**(n-1)-1
min_=0
while(index<=emp):
    if sum_(index) == m:
        min_ = index
        break
    index+=1
if len(str(min_)) < n:
    min_=max_
print(min_,max_)

