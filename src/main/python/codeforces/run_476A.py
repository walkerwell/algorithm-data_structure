#coding=utf-8
n,m=map(int,raw_input().split())
# 步数有上限和下限 从下限往上找第一个m的倍数就是答案
if n>=m:
    for _ in range((n+1)/2,n+1):
        if _%m==0:
            print _
            break
else:
    print -1