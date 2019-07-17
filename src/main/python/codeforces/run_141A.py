a=input()
b=input()
c=input()
if len(a)+len(b) != len(c):
    print("NO")
    exit(0)
use = [0]*len(c)
find_a=0
find_b=0
for i in a:
    for j,value in enumerate(c):
        if use[j]==0 and i == value:
            use[j] = 1
            find_a+=1
            break
for i in b:
    for j,value in enumerate(c):
        if use[j]==0 and i == value:
            use[j] = 1
            find_b+=1
            break
if find_a == len(a) and find_b == len(b):
    print("YES")
else:
    print("NO")

# the better code is
if sorted(input() + input()) == sorted(input()):
    print('YES')
else:
    print('NO')
