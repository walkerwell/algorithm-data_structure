def maxx(a,b):
    if a==1 or b==1:
        return 1
    if a<=0 or b<=0:
        return 100
    if a%b==0:
        return b
    elif b%a==0:
        return a
    res=1
    emp=1
    it = max(a,b)
    for i in range(it):
        if a%res==0 and b%res==0:
            emp = res
        res+=1
    return emp
a,b,n=map(int,raw_input().split())
left=n
while(True):
    left = left - maxx(a,left)
    if left<0:
        print 1
        break
    left = left - maxx(b,left)
    if left<0:
        print 0
        break



