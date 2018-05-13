# -*- coding:utf-8 -*-
n,cost = map(int,raw_input().split(" "))
sum_min = 60 * 4
res=0
while(sum_min>=0 and n>0):
	res+=1
	n-=1
	sum_min-=(5*res)
print(res)