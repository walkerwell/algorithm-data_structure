k,r=map(int,raw_input().split())
res=1
emp=0
while(True):
    emp = res*k
    left = emp%10
    if left==0 or left==r:
        break
    res+=1
print res