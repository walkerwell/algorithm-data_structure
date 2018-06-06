n,m=map(int,raw_input().split())
day=n
while(True):
    if day==n+day/m:
        print day
        break
    day+=1

## 460A==379A