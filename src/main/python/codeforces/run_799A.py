# -*- coding:utf-8 -*-
# 将每行最小和每列最小再输入的时候选出来
matrix= map(int,raw_input().split())
sum = matrix[0]
each_time=matrix[1]
each_time_bake_num=matrix[2]
second_oven_build_time=matrix[3]
if sum <  each_time_bake_num:
    print "NO"
    exit(0)
one_oven_bake_num = (sum+each_time_bake_num-1)/each_time_bake_num
if one_oven_bake_num < 2:
    print "NO"
    exit(0)
one_oven_use_time=one_oven_bake_num * each_time
emp=0
emp = each_time - second_oven_build_time
if one_oven_use_time <= (each_time + second_oven_build_time - emp):
    print "NO"
    exit(0)
print "YES"
