n=input()
x=0
y=0
z=0
for i in range(n):
    x1,y1,z1=(map(int,raw_input().split()))
    x+=x1
    y+=y1
    z+=z1
if((x|y|z)==0):
    print "YES"
else:
    print "NO"
