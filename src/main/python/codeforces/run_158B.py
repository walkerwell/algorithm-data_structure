n=input()
a=map((int),raw_input().split())
a.sort()
res=0
mark=[]
for i in range(n):
    mark.append(1)
index=len(a)-1
while(index>-1):
    if(mark[index]==1):
        sum=a[index]
        for i in range(index):
            # print(i)
            if(mark[i]==1 and (sum+a[i])<5):
                sum+=a[i]
                mark[i]=0
                # print(mark)
        res+=1
        mark[index]=0
        # print index,a[index],sum
    index-=1
print res