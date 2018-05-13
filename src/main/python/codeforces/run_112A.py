m=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def find(a):
    for i in range(len(m)):
        if(m[i]==a):
            return i
a=raw_input()
b=raw_input()

res=0
for i in range(len(a)):
    if(find(a[i].lower()) > find(b[i].lower())):
        res=1
        break
    elif(find(a[i].lower()) < find(b[i].lower())):
        res=-1
        break
print(res)