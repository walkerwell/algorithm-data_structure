n,l=map(int,raw_input().split())
m=map(int,raw_input().split())
matrix=[0]*(l+1)
for emp in m:
    matrix[emp]=1
len=[0]*(l+1)
len_index=0
double_=True
for i in range(l):
    if matrix[i]==matrix[i+1]:
        if double_:
            len[len_index]=2
            double_=False
        else:
            len[len_index]=len[len_index]+1
    else:
        len_index+=1
        double_=True
# print matrix
# print len
xam=max(len)
xam_index=len.index(xam)
if xam_index==0 or xam_index+xam==l:
    print "%.10f" % xam
else:
    print "%.10f" % ((xam+1)/2.0)