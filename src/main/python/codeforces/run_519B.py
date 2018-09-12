#coding=utf-8
# 这道题不要想复杂了，就是每组数相加 s1 s2 s3  s1-s2 s2-s3 就是结果 结果想复杂了
# 原来想多了导致复杂的算法看CF的提交记录
n=input()
a=sum(map(int,raw_input().split()))
b=sum(map(int,raw_input().split()))
c=sum(map(int,raw_input().split()))
print a-b
print b-c