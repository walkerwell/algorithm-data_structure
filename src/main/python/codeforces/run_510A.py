import sys
n,m=map(int,raw_input().split())
isHead=False
for i in range(n):
    if (i+1)%2<>0:
        for j in range(m):
            sys.stdout.write("#")
    else:
        for j in range(m):
            if isHead and j==0:
                sys.stdout.write("#")
            elif ~isHead and j==m-1:
                sys.stdout.write("#")
            else:
                sys.stdout.write(".")
        isHead=~isHead
    print ""
