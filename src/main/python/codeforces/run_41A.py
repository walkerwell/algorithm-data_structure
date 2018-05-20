a=raw_input()
b=raw_input()
if(len(a)<>len(b)):
    print "NO"
    exit(0)
else:
    index=len(a)-1
    i=0
    while(index>=0):
        if(a[i]<>b[index]):
            print "NO"
            exit(0)
        index-=1
        i+=1
    print "YES"