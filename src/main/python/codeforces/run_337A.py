n,m = map(int,input().split())
array = list(map(int,input().split()))
array.sort()
diff=999999999999
min_index=0
max_index=0
for i in range(m-n+1):
    if array[i+n-1] - array[i] <diff:
        min_inde = i
        max_index = i+n-1
        diff = array[i+n-1] - array[i]
print(diff)