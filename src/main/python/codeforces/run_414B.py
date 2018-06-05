n,k = map(int,raw_input().split())
e = 1000000007
def solve(x):
    r = []
    for i in xrange(1,int(x**0.5)+1,1):
        if x%i==0:
            if i==x/i:
                r.append(i)
            else:
                r.extend([i,x/i])
    return r
r1 = []
for i in xrange(1,n+1,1):
    r1.append(solve(i))
#print r1
s = [[0]*n for _ in xrange(k)]
for i in xrange(k):
    for j in xrange(n):
        if i==0:
            s[i][j]=1
        else:
            if j==0:
                s[i][j]=1
            else:
                for w in r1[j]:
                    s[i][j]=(s[i][j]+s[i-1][w-1])%e
print sum(s[k-1])%e
print s[0]
print s[1]
print s[2]
print s[3]