n,x=map(int,raw_input().split())
count=0
for i in xrange(1,n+1):
    if x/i<=n and x/i*i==x:
        count+=1
print count