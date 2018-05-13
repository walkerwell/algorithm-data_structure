# -*- coding:utf-8 -*-
sum=(int)(input())
str=raw_input()
count=0
index=0
while(True):
    if(index>=sum-1):
        if(index==sum-1):
            count+=1
        break
    if(str[index] == 'U' and str[index+1] == 'R'):
        count+=1
        index+=2
    elif(str[index] == 'R' and str[index+1] == 'U'):
        count+=1
        index+=2
    else:
        count+=1
        index+=1
print(count)