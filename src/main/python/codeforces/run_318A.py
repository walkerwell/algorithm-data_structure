n,k=map(int,raw_input().split())
middle=0
if n%2==0:
    middle=n/2
else:
    middle=(int)(n/2.0+0.9)
if k<=middle:
    print 1+((k-1)*2)
else:
    print 2+((k-middle-1)*2)