n=input()
a=map(int,raw_input().split())
odd=0
even=0
index=0
while(index<=n-3):
    if (a[index]%2!=0 and a[index+1]%2!=0 and a[index+2]%2!=0):
        index+=1
        continue
    if (a[index]%2+a[index+1]%2+a[index+2]%2)!=0:
        if(a[index]+a[index+1]+a[index+2])%2==0:
            if(a[index]%2==0):
                print index+1
            elif(a[index+1]%2==0):
                print index+2
            else:
                print index+3
        else:
            if(a[index]%2!=0):
                print index+1
            elif(a[index+1]%2!=0):
                print index+2
            else:
                print index+3
        exit(0)
    index+=1