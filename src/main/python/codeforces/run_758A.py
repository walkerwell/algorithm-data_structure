n=input()
m=map(int,input().split())
max_=max(m)
res=0
for a in m:
    res+=abs(max_-a)
print (res)