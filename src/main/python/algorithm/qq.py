def quick(m):
    sort(m,0,len(m)-1)

def sort(m,low,high):
    if low>=high:
        return
    j = partition(m,low,high)
    sort(m,low,j-1)
    sort(m,j+1,high)

def partition(m,low,high):
    i=low+1
    j=high
    v=m[low]
    while(True):
        while(i<=j):
            if m[i]<= v:
                break
            i+=1
        while(i<=j):
            if m[j] >= v:
                break
            j-=1
        if i>=j:
            break
        exchange(m,i,j)
    exchange(m,low,j)
    return j

def exchange(m,i,j):
    e = m[i]
    m[i] = m[j]
    m[j] = e

m=[3,345,23,42,34,233,24,23,234,2,23,23,4,5,6,3,2,6,4,235,7,568,3,34,6,3,35]
quick(m)
print(m)