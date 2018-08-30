n=input()
m=[]
emp={}
for i in range(n):
    name = raw_input()
    if name in emp:
        num = emp[name]
        print name+(str)(num)
        emp[name]=num+1
    else:
        emp[name]= 1
        print "OK"

