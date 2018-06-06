s=raw_input()
a=[0]
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        a.append(a[-1]+1)
    else:
        a.append(a[-1])
n=input()
for _ in range(n):
    b,e=map(int,raw_input().split())
    print a[e-1]-a[b-1]