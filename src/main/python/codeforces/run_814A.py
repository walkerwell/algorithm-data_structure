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
# 此题的题目含义是将b数组插入到A数组，直到A数组是非递增的就可以
# 将B排序后，reverse
# 再往A中插入，每次插入判断前后两个数组是否是递减的 递减就返回YES 程序结束
# 当循环A数据结束 说明没有找到非递增数组，则NO