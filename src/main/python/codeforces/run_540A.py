n=input()
s1=raw_input()
s2=raw_input()
res=0
for i in range(n):
    a1=(int)(s1[i])
    a2=(int)(s2[i])
    max_=max(a1,a2)
    min_=a1+a2-max_
    res+=min(max_-min_,min_+10-max_)
print res