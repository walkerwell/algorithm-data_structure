n,a,b,c=map(int,raw_input().split())
if a+b+c ==n :
    print 3
elif a+b == n or a+c==n or b+c==n:
    print 2
elif a==n or b==n or c==n:
    print 1
elif a==b==c==1:
    print n
else:
    print n/(a+b+c)*3