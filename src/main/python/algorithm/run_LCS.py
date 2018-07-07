def findTheMax(matrix):
    index=0
    res=matrix[0]
    for i in range(len(matrix)):
        if matrix[i]>res:
            res=matrix[i]
            index=i
    return res,index
def findDPMatrix(matrix):
    dp=[]
    for i in range(len(matrix)):
        n=1
        j=i-1
        now_=matrix[i]
        while(j>=0):
            if now_>matrix[j]:
                n+=1
                now_=matrix[j]
            j-=1
        dp.append(n)
    return dp
matrix=[2,3,5,9,6]
dp=findDPMatrix(matrix)
print dp
a,b = findTheMax(dp)
print a,b
index=b-1
res=""+(str)(matrix[b])
now_=matrix[b]
while(index>=0):
    if(matrix[index]<now_):
        res+=(str)(matrix[index])
        now_=matrix[index]
        index-=1
print res
