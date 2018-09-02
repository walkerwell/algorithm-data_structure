n=input()
for i in range(n):
    a=(int)(raw_input())
    if 360%(180-a)==0:
        print "YES"
    else:
        print "NO"