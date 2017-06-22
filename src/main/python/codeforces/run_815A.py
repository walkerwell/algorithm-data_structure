# -*- coding:utf-8 -*-
# 将每行最小和每列最小再输入的时候选出来
n,m= map(int,raw_input().split())
a =[]
for x in xrange(m):a.append(0)
for i in xrange(1,n+1):
	max_=0
	min_=2147483647
	col=1
	col_max =[]
	for x in xrange(m):col_max.append(0)
	row = map(int,raw_input().split())
	for num in row:
		if min_ > num:
			min_ = num
			max_ = min_
		if max_ < num:
			max_ = num
			col_max[col-1] = max_
		col+=1
	if col_max[col-1] >0 and col_max[col-1] == max_:
		print -1
		exit()
	for _ in xrange(min_):print 'row '+(str)(i)
	if max_ > min_ and a[col-2]!=1:
			for _ in xrange(max_-min_):print 'col '+(str)(col-2)
			a[col-2]=1