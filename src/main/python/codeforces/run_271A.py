n=input()
i=n+1
def isRes(a):
    s=[a/1000,a/100%10,a/10%10,a%10]
    for i in range(0,4):
        for j in range(i+1,4):
            if s[i]==s[j]:
                return False
    return True
while(i<9999):
    if isRes(i):
        print i
        break
    i+=1