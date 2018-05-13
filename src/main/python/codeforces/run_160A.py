n=input()
a=map(int,raw_input().split())
a.sort(reverse=True)
for i in range(n-1):
    if(sum(a[:i+1]) > sum(a[i+1:])):
        # print i,sum(a[:i]),sum(a[i+1:])
        print i+1
        exit(0)
print n