n=input()
if n<3:
    print "No"
else:
    print "Yes"
    mid = (n+1)/2
    print "1 "+(str)(mid)
    print n-1,
    for _ in range(1,n+1):
        if _<>mid:
            print _,
