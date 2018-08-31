n=input()
emp=0
i=1
while(True):
    plus=(i*(i+1))/2
    if emp+plus>n:
        break
    else:
        i+=1
        emp+=plus
print i-1