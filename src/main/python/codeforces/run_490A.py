n = int(input())
m = [int(i) for i in input().split()]
mm = {}
for i,value in enumerate(m):
    if value in mm:
        mm[value][0] +=1
        mm[value][1].append(i+1)
    else:
        mm[value] = []
        mm[value].append(1)
        mm[value].append([i+1])
if 1 in mm and 2 in mm and 3 in mm:
    iter = min(mm[1][0],mm[2][0],mm[3][0])
    print(iter)
    for i in range(iter):
        print(mm[1][1][i],mm[2][1][i],mm[3][1][i])
else:
    print(0)