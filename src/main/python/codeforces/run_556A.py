n=input()
s=raw_input()
zero=0
for _ in s:
    if _ =='0':
        zero+=1
if zero*2==n:
    print 0
else:
    print abs(n-zero*2)
