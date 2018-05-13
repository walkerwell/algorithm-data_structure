a=map(int,raw_input().split())
s=map(int,raw_input().split())
num=0
for i in range(a[0]):
    if(s[i]<>0 and s[i]>=s[a[1]-1]):
        num+=1
    else:
        break
print(num)

