sum=input()
n=map(int,raw_input().strip().split(" "))
for i in range(sum):
    if(i>=sum):
        break
    if n[i]==1:
        print -1
        exit(0)
print 1