n=input()
a=[5,4,3,2,1]
emp=0
while(n>0):
    for i in a:
        if(n-i>=0):
            n-=i
            emp+=1
            break
print emp