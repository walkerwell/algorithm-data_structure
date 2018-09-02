ma=[ 'C', 'M', 'Y']
n,m=map(int,raw_input().split())
res=True
for i in range(n):
    s=raw_input().split()
    for a in s:
        if a in ma:
            res=False
            break
if res:
    print "#Black&White"
else:
    print "#Color"