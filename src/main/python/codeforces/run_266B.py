a,x=map(int,raw_input().split())
s=raw_input()
if(s.find('G')==-1):
    print s
    exit(0)
res=""
usedIndex=[]
for i in range(x):
    index=0
    res=""
    while(index<a-1):
        if(s[index]=='B' and s[index+1]=='G'):
            res+="GB"
            index+=2
        else:
            res+=s[index]
            index+=1
    # print index,len(s),res
    if(index<>a):
        res+=s[index]
    s=res
    # print "s is :",s
print res
