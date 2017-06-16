__author__ = 'wubo'
matrix = []
for _ in xrange(4):
    matrix.append(map(int,raw_input().split()))
if matrix is not None and len(matrix)==4:
    for index in [0,1,2,3]:
        if matrix[index][3] == 1:
            one =   index+1 if (index+1)<=3  else (index+1)^4
            two =   index+2 if (index+2)<=3  else (index+2)^4
            three = index+3 if (index+3)<=3  else (index+3)^4
            if (matrix[index][0]|matrix[index][1]|matrix[index][2])|matrix[one][0]|matrix[two][1]|matrix[three][2] == 1:
                print("YES")
                exit(0)
print("NO")

# 加一与4异或  为的就是取二进制的后两位，但是用异或的话，还在增加额外判断+1是否大于3，大于3的才会参与异或，不大于3的直接+1就好
# 实际上就是取余%4的操作
p = []
for _ in xrange(4):
  p.append(map(int,raw_input().split()))
#print p
for i in xrange(4):
  if p[i][3] == 1:
    if p[i][0]+p[i][1]+p[i][2]+p[(i+1)%4][0]+p[(i+2)%4][1]+p[(i+3)%4][2]>0:
      print 'YES'
      exit(0)
print 'NO'