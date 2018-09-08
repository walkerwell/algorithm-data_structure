n=input()
m=map(int,raw_input().split())
minOne=999
minIndex=0
maxOne=-1
maxIndex=0
index=0
for a in m:
    if a <= minOne:
        minOne = a
        minIndex = index
    if a > maxOne:
        maxOne = a
        maxIndex = index
    index+=1
if minIndex<maxIndex:
    if (minIndex+1) == maxIndex and n==2:
        print 1
    # elif minIndex+1 == maxIndex:
    #     print n-minIndex+maxIndex-1
    else:
        print n-minIndex+maxIndex-2
else:
    if minIndex==n-1 and maxIndex==0:
        print 0
    else:
        print n-minIndex+maxIndex-1