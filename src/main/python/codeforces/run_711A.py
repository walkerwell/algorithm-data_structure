n=input()
res=True
s=""
for _ in range(n):
    a = raw_input().split("|")
    if res and a[0]=="OO":
        res=False
        s+="++|"
    else:
        s+=a[0]+"|"
    if res and a[1]=="OO":
        res=False
        s+="++"
    else:
        s+=a[1]
    s+="\n"
if res:
    print "NO"
else:
    print "YES"
    print s