s=raw_input()
index=0
mark="hello"
emp=""
for i in s:
    if(i==mark[index]):
        # print i
        emp+=i
        index+=1
    if(index>4):
        break
if(emp==mark):
    print "YES"
else:
    print "NO"
