# -*- coding:utf-8 -*-
# 刚开始时想错了，想成了 排列组合，
# 实际上时 1.看x，y是否是两坐标差的倍数,2.并且是相同的变动倍数
# 不明白为什么需要变动相同的倍数时 要判断 变动倍数与2做取余操作后相等
# 是不是这个意思  A往前走一步，A再后退一步；B前进两步，这个时候不能说A没动，A与B都是变动了两倍数?
# 根据题意，两个数的相加减是互不影响的
a,b,c,d = map(int,raw_input().strip().split())
x,y = map(int,raw_input().strip().split())
if (c-a)%x == 0 and (d-b)%y==0 and (c-a)/x%2==(d-b)/y%2:
    print "YES"
else:
    print "NO"