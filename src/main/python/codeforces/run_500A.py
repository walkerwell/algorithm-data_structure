n,target=map(int,raw_input().split())
m=map(int,raw_input().split())
index=0
while(True):
    if index+1 > target:
        print "NO"
        exit(0)
    elif index+1 == target:
        print "YES"
        exit(0)
    index+=m[index]
