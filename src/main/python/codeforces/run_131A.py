s=raw_input()
allUp=1
otherUp=1
for i in range(len(s)):
    if(s[i].islower()):
        allUp=0
    if(i<>0 and s[i].islower()):
        otherUp=0
res=""
for i in range(len(s)):
    if(allUp or otherUp):
        if(s[i].isupper()):
            res+=s[i].lower()
        else:
            res+=s[i].upper()
    else:
        res=s
        break
print res