# n=input()
# a=map(int,input().split())
# emp={}
# for _ in a:
#     if _ in emp:
#         emp[_] +=1
#     else:
#         emp[_] = 1
# for i in range(1, 5):
#     if i not in emp:
#         emp[i] = 0
# res = emp[4]
# if emp[1] > 0 and emp[3] > 0:
#     min_ = min(emp[1], emp[3])
#     cost_1 = min_
#     if emp[1] < min_:
#         cost_1 = emp[1]
#     res += (cost_1 + 3*min_)//4
#     emp[1] -= cost_1
#     emp[3] -= min_
# if emp[2] > 1:
#     car = emp[2] // 2
#     res += car
#     emp[2] -= car*2
# if emp[1] > 0 and emp[2] > 0:
#     min_ = min(emp[1], emp[2])
#     cost_1 = min_*2
#     if emp[1] < min_*2:
#         cost_1 = emp[1]
#     res += ( cost_1 + 2*min_ + 3)//4
#     emp[1] -= cost_1
#     emp[2] -= min_
# if emp[1] > 0:
#     res += (emp[1] + 3) // 4
# if emp[2] > 0:
#     res += (emp[2]+1) // 2
# if emp[3] > 0:
#     res += emp[3]
# print(int(res))

# better code
n=int(input())
a,b,c,d = map(input().split().count,['1','2','3','4'])
print( (max(a-c,0)+b*2+3)//4 + c + d )