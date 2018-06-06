n=input()
s=raw_input()
if n>=26:
    a={}
    for i in range(n):
        a[s[i].lower()]=1
    if len(a)==26:
        print "YES"
        exit(0)
print "NO"