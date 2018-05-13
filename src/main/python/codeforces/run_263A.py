row=0
col=0
for i in range(5):
    s=raw_input()
    res=s.find("1")
    if(res<>-1):
        row=i
        a=map(int,s.split())
        for emp in range(5):
            if(a[emp]==1):
                col=emp
print abs(row-2)+abs(col-2)