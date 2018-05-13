a=input()
res=0
for i in range(a):
    if(sum(map(int,raw_input().split()))>=2):
        res+=1
print res
