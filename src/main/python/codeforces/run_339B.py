n,m=map(int,raw_input().split())
matrix=map(int,raw_input().split())
res=matrix[0]-1
a=matrix[0]
for i in range(1,m):
    b=matrix[i]
    if b>=a:
        res+=b-a
    else:
        res+=n-a+b
    a=matrix[i]
print res
