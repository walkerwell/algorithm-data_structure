n,k=map(int,raw_input().split())
m=map(int,raw_input().split())
emp=[]
for a in m:
    if a+k<=5:
        emp.append(a)
print len(emp)/3