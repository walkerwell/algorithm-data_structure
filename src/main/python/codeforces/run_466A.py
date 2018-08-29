n,m,a,b=map(int,raw_input().split())
time = n*a
n_cost=0
if n<m:
    n_cost=b
else:
    n_cost=n/m*b
    if n%m<>0:
        if n%m*a<b:
            n_cost+=n%m*a
        else:
            n_cost+=b
if time<n_cost:
    print time
else:
    print n_cost