# -*- coding:utf-8 -*-
n,m = map(int,raw_input().split())
a = map(int,raw_input().split())
b = map(int,raw_input().split())
b = sorted(b,reverse=True)
bIndexMark =0;
for index in xrange(0,len(a)-1):
    if a[index] ==0:
        a[index] = b[bIndexMark]
        bIndexMark+=1
    if a[index+1] == 0:
        a[index+1] = b[bIndexMark]
        bIndexMark+=1
    if a[index] > a[index+1]:
        print("YES")
        exit(0)
print("NO")