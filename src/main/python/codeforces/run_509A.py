n=input()
m=[]
# n^2 复杂度 可以降低成N的复杂度
for i in range(n):
    m.append(1)
for i in range(1,n):
    for j in range(n):
        if j==0:
            m[j]=1
        else:
            m[j]=m[j-1]+m[j]
print m[n-1]