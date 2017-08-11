# -*- coding:utf-8 -*-
charSum,oneV1,twoV1,oneV2,twoV2= map(int,input().strip().split())
first = charSum*oneV1+oneV2*2
second = charSum*twoV1+twoV2*2
if first<second:
    print ('First')
elif first>second:
    print ('Second')
else:
    print ('Friendship')