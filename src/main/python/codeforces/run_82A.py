n=input()
m = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
sqr=2
all_num=0
has_num=0
while(True):
    all_num+=2**sqr+2**(sqr-2)
    if all_num>=n:
        break
    has_num=all_num
    sqr+=1
left_num=n-has_num
ever_num=2**(sqr-2)
# print has_num,sqr,left_num,ever_num
print m[(left_num+ever_num-1)/ever_num-1]