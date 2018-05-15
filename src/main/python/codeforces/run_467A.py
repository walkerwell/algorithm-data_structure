n=input()
res=0
for i in range(n):
    now,total=map(int,raw_input().split())
    if((now+2)<=total):
        res+=1
print res