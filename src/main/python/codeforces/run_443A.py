s=raw_input()
m={}
n=len(s)
ignore=['{',',',' ','}']
for i in range(n):
    if s[i] not in ignore:
        m[s[i]]=s[i]
print len(m)