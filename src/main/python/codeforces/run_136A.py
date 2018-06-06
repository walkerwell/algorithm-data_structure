n=input()
a=map(int,raw_input().split())
res= [0]*n
for i in range(n):
    res[a[i]-1]=i+1
for i in res:
    print i,