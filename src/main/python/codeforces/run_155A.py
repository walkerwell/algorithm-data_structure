n=input()
m=map(int,raw_input().split())
res=0
maxN=m[0]
minN=m[0]
for i in range(1,len(m)):
    a = m[i]
    if a <minN:
        res+=1
        minN = a
    elif a>maxN:
        res+=1
        maxN = a
print res