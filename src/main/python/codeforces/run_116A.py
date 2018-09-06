n = input()
res=0
now=0
for _ in range(n):
    a,b=map(int,raw_input().split())
    now=now+b-a
    if now>res:
        res=now
print res