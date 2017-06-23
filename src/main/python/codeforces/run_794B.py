# -*- coding:utf-8 -*-
# 题解思路是 利用相似三角形的 相似比的平方 == 面积比
n,h= map(int,raw_input().strip().split())
for i in xrange(1,n):
    print(i*1.0/n)**0.5*h,