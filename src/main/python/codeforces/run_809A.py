# -*- coding:utf-8 -*-
N = int(raw_input().strip())
m = sorted(map(int,raw_input().strip().split()),reverse=True)
result=0
mid_num=1
a=1000000007
for index in xrange(N):
    result+=mid_num*(m[N-1-index]-m[index])%a
    mid_num=mid_num*2%a
print(result%a)