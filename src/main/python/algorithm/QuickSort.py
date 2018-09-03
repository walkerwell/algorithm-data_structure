#coding:utf-8
def quick(matrix):
    # 正因为快排对于倒叙的数组排序性能很差，所以导致原始的快排以来输入数据，
    # 那我这里我们就有 随机性来解决此问题
    # 一、随机性的两种实现
    # 1 在此处随机打乱数组
    # 2 在partition中随机选择切分元素、以达到随机性
    # 二、避免算法在有重复元素的时候陷入n方级别
    # 1 在partition的比较是否交换的时候加上>= 和 <=
    sort(matrix,0,len(matrix)-1)

def sort(matrix,low,high):
    if low>=high:
        return
    j = partition(matrix,low,high)
    sort(matrix,low,j-1)
    sort(matrix,j+1,high)

def partition(matrix,low,high):
    i=low
    j=high
    v = matrix[low]
    while(True):
        while(i<=j):
            if(matrix[i]>=v): # 1.大于等于决定升序还是降序(见qq.py) 2.加上等于的判断避免算法在大量重复的元素是陷入N方级别
                break
            i+=1
        while(i<=j):
            if matrix[j]<=v: # 1.大于等于决定升序还是降序(见qq.py) 2.加上等于的判断避免算法在大量重复的元素是陷入N方级别
                break
            j-=1
        if(i>=j):
            break
        exchange(matrix,i,j)
    exchange(matrix,low,j)
    return j

def exchange(matrix,i,j):
    emp = matrix[i]
    matrix[i] =matrix[j]
    matrix[j] = emp


m=[3,345,23,42,34,233,24,23,234,2,23,23,4,5,6,3,2,6,4,235,7,568,3,34,6,3,35]
quick(m)
print(m)