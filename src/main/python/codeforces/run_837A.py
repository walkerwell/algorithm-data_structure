# -*- coding:utf-8 -*-
num=(int)(input().strip())
a=input().strip()
upper_a=a.upper()
upper_num=0
final_num=0
for index in range(0,num):
    if a[index]!=' ' and a[index]==upper_a[index]:
        upper_num+=1
    if final_num < upper_num:
        final_num=upper_num
    if a[index]==' ':
        upper_num=0
print(final_num)
##最简单的方法：
##1.直接按照空格分开单词，
##2.遍历单词，看每个单词的大写字母个数   a.isUpper() 用来判断字符是否是大写字符
##3.选出一个最多的字母个数