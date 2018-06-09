n,h=map(int,raw_input().split())
m=map(int,raw_input().split())
res=0
for a in range(n):
    if m[a] <= h:
        res+=1
    else:
        res+=2
print res