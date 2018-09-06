n=input()
m=0
c=0
for i in range(n):
    m_,c_=map(int,raw_input().split())
    if m_ > c_:
        m+=1
    elif m_ < c_:
        c+=1
if m>c:
    print "Mishka"
elif m<c:
    print "Chris"
else:
    print "Friendship is magic!^^"