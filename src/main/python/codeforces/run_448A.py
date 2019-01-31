cup_sum=sum(map(int,raw_input().split()))
me_sum=sum(map(int,raw_input().split()))
n=input()
me_need_shelf=(me_sum+9)/10
cup_need_shelf=(cup_sum+4)/5
if me_need_shelf+cup_need_shelf > n:
    print "NO"
else:
    print "YES"