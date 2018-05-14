s=raw_input()
a=[0]*26
for i in s:
    a[ord(i)-97]=1
res=sum(a)
if(res%2==0):
    print "CHAT WITH HER!"
else:
    print "IGNORE HIM!"