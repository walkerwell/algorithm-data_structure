boy=int(input())
boy_skill=[int(i) for i in input().split()]
list.sort(boy_skill)
girl=int(input())
girl_skill=[int(i) for i in input().split()]
list.sort(girl_skill)
res=0
for i,boy_value in enumerate(boy_skill):
    for j,girl_value in enumerate(girl_skill):
        if abs(boy_value-girl_value) <= 1:
            res += 1
            girl_skill[j] = 9999
            break
print(res)
# try dp do this