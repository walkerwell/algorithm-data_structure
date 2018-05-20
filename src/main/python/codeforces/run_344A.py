n=input()
res=1
last="aa"
for i in range(n):
    now=raw_input()
    if last[1]==now[0]:
        res+=1
    last=now
print res
