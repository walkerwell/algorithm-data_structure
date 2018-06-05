# n=input()
# def isLucky(n):
#     s=""+(str)(n)
#     for i in s:
#         if(i<>'4' and i<>'7'):
#             return False
#     return True
# for i in range(n+1):
#     if(isLucky(i) and n%i==0):
#         print "YES"
#         exit(0)
# print "NO"
lucky=[4,7,47,74,447,474,477,744,747,774]
n=input()
for i in lucky:
    if n%i==0:
        print "YES"
        exit(0)
print "NO"