def binarySearch(n,matrix):
    left=0
    right=len(matrix)-1
    while(left<>right):
        index=(int)((right+left)/2.0+0.5)
        if n==matrix[index]:
            return index
        elif n<matrix[index]:
            right=index
        else:
            left=index
    return -1
print binarySearch(100,[1, 2, 3, 4, 100])