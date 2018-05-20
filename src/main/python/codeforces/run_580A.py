n=input()
m=map(int,raw_input().split())
res=0
resM=[]
for i in range(n-1):
    if m[i]<=m[i+1]:
        if res>0:
            isContinue=True
        res+=1
        # print m[i],m[i+1],res
    else:
        resM.append(res+1)
        res=0
if len(resM)>0:
    print max(max(resM),res+1)
else:
    print res+1