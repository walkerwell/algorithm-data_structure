def mergeSort(a):
    sort(a,0,len(a))

def sort(a,low,high):
    if low>=high:
        return
    mid = low+ (high-low)/2
    sort(a,low,mid)
    sort(a,mid+1,high)
    merge(a,low,mid,high)

def merge(a,low,mid,high):
    i=low
    j=mid+1
    aux = []
    for k in range(len(a)):
        aux.append(a[k])
    print aux
    print range(low,high)
    for k in range(len(a)):
        if(i>mid):
            a[k] = aux[j]
            j+=1
        elif(j>high):
            a[k] = aux[i]
            i+=1
        elif(aux[i]>aux[j]):
            a[k] = aux[j]
            j+=1
        else:
            a[k] = aux[i]
            i+=1

m=[345,3,23,12,34,233,24,23,234,2,23,23,4,5,6,3,2,6,4,235,7,568,3,34,6,3,35]
mergeSort(m)
print(m)
