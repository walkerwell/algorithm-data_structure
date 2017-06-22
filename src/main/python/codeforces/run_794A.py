# -*- coding:utf-8 -*-
a,b,c= map(int,raw_input().strip().split())
N = int(raw_input().strip())
matrix = map(int,raw_input().strip().split())
num =0
for s in matrix:
    if s > b and s <c:
        num+=1
print(num)
