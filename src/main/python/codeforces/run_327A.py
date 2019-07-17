# n = int(input())
# array = input().split()
# one_index = []
# m = []
# max_zero=0
# row=0
# col=0
# for i in range(n):
#     emp = [0] * n
#     if array[i] == "1":
#         one_index.append(i)
#         emp[i] = 0
#     else:
#         emp[i] = 1
#     m.append(emp)
#     for j in range(i,n):
#         if array[j] == "1":
#             m[i][j] = m[i][j-1] - 1
#         else:
#             m[i][j] = m[i][j-1] + 1
#         if m[i][j] >= max_zero:
#             row, col = i, j
#             max_zero = m[i][j]
# # print("row:",row,"col:",col)
# # print(one_index)
#
# res = col-row + 1 + len(one_index)
# for _ in one_index:
#     if _ >= row and _ <= col:
#         res -= 2
# print(res)
# for i in range(n):
#     s=""
#     for j in range(n):
#         s+=str(m[i][j])+" "
#     print(s)


# another better code
n=int(input())
array=[int(i) for i in input().split()]
x=sum(array)
current_zero=0
old_zero=0
for i in array:
    if i == 0:
        current_zero += 1
        if current_zero > old_zero:
            old_zero = current_zero
    elif current_zero>0:
        current_zero -= 1
    print(current_zero,old_zero)
if old_zero == 0:
    old_zero -= 1
print(x+old_zero)


