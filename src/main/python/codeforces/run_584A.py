n,t=map(int,raw_input().split())
min_=(10**(n-1))+1
max_=(10**n-1)
emp=max_
while(emp>=min_):
    if emp>=min_ and emp<=max_ and emp%t==0:
        print emp
        exit(0)
    emp-=1
print -1