n=input()
a=[]
b=[]
for _ in range(n):
    aa,bb=map(int,raw_input().split())
    a.append(aa)
    b.append(bb)
res=0
for i in range(n):
    for j in range(i+1,n):
        if a[i]==b[j]:
            res+=1
        if b[i]==a[j]:
            res+=1

print res