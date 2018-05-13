n=input()
s=raw_input()
res=0
for i in range(n-1):
    if(s[i]==s[i+1]):
        res+=1
print res