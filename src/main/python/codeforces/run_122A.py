s=raw_input()
other=0
for i in s :
    if (i<>'4' and i<>'7'):
        other=1
        break
if(other==0):
    print "YES"
else:
    a=int(s)
    if(a%4==0 or a%7==0):
        print "YES"

    else:
        print "NO"