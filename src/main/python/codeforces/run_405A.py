# -*- coding:utf-8 -*-
## 自定义排序算法
def maopao(a,aLen):
    for emp in range(aLen-1):
        for i in range(aLen-emp-1):
            if a[i]>a[i+1]:
                a[i]+=a[i+1]
                a[i+1]=a[i]-a[i+1]
                a[i]=a[i]-a[i+1]
    return a


n=input()
a=map(int,raw_input().split())
a=maopao(a,n)
res=""
for i in a:
    res+=(str)(i)+" "
print res

