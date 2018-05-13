sum=input()
s=[]
for i in range(sum):
    s.append(raw_input())
for i in range(sum):
    if(len(s[i])<=10):
        print(s[i])
    else:
        print((str)(s[i][0])+(str)(len(s[i])-2)+(str)(s[i][-1]))