s=raw_input()
res=0
for i in s:
    if(i=='4' or i=='7'):
        res+=1
if(res ==7 or res==4):
    print "YES"
else:
    print "NO"