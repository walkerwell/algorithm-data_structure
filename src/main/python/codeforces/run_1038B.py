#coding=utf-8
#解题思路：原题是要找两个集合的最大公约数  就是找中位数  中位数最好找 就是题解的一种
n=input()
if n<3:
    print "No"
else:
    print "Yes"
    mid = (n+1)/2
    print "1 "+(str)(mid)
    print n-1,
    for _ in range(1,n+1):
        if _<>mid:
            print _,
