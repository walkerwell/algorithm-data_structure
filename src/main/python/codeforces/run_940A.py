# -*- coding:utf-8 -*-
num_sum,d = map(int,raw_input().strip().split(" "))
all = map(int,raw_input().strip().split(" "))
if len(all)<1:
    print 0
all = sorted(all)
head=0
tail=len(all)-1
large_res=0
smail_res=0
# print all
# print all[head]
while(True):
    if (all[tail]-all[head]) > d:
        large_res+=1
    else:
        break
    head+=1
head=0
while(True):
    if (all[tail]-all[head]) > d:
        smail_res+=1
    else:
        break
    tail-=1
print large_res,smail_res
if large_res < smail_res:
    print large_res
else:
    print smail_res