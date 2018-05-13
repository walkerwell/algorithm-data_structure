s=raw_input()
sameNum=1
lastChar=''
for i in range(len(s)):
    if(s[i]==lastChar):
        sameNum+=1
    else:
        sameNum=1
    if(sameNum>=7):
        print "YES"
        exit(0)
    lastChar=s[i]
print "NO"