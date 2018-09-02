sum_=sum(map(int,raw_input().split()))
if sum_%5==0 and sum_<>0:
    print sum_/5
else:
    print -1
