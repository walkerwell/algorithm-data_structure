s,n=map(int,raw_input().split())
res=False
for i in range(n):
    x,y=map(int,raw_input().split())
    if s>=x:
        s+=y
        if i==n-1:
            res=True
if res:
    print "YES"
else:
    print "NO"