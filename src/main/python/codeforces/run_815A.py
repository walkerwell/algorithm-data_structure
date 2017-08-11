# -*- coding:utf-8 -*-
# 将每行最小和每列最小再输入的时候选出来
n,m= map(int,raw_input().split())
a=[]
for _ in xrange(n):
	a.append(map(int,raw_input().split()))
res=""
res_num=0
for i in xrange(n):
	for _ in xrange(m):
		min_ = 2147483647
		max_ = 0
		max_index=0
		#先找出每行的最小值最大值
		for j,num in enumerate(a[i]):
			if num < min_:
				min_ = num
			if num > max_:
				max_ = num
				max_index=j
		# 为了区分 先变更行 还是先变更列
		if n<=m:
			# 再把每行进行相应的减少
			for _ in xrange(min_):
				for j,num in enumerate(a[i]):
					a[i][j] = a[i][j]-1
				res += 'row ' + (str)(i+1) +'\n'
				res_num+=1
		#将行列转置后 检查每列是否合法
		zip_a = zip(*a)
		min_ = 2147483647
		max_ = 0
		for j,num in enumerate(zip_a[max_index]):
			if num < min_:
				min_ = num
		for _ in xrange(min_):
			for j, num in enumerate(zip_a[max_index]):
				a[j][max_index] = a[j][max_index] - 1
			res += 'col ' + (str)(max_index+1) + '\n'
			res_num += 1
			#TODO 需要减列之后再考虑在行上进行判断
	# 检查最后的结果是否符合规范
for i in xrange(n):
	for num in a[i]:
		if num != 0:
			print -1
			exit()
#输出结果时需要区分 正确结果 >0 =0 的情况 & 不存在结果的情况
if res_num>0:
	print res_num
	print res
elif res_num==0:
	print "0"