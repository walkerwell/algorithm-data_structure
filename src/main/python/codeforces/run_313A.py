n=input()
if n>0:
    print n
else:
    s=(str)(n)
    delIndex=len(s)-1
    if s[len(s)-1]<s[len(s)-2]:
        delIndex = len(s)-2
    if(delIndex>=len(s)-1):
        print int(s[0:delIndex])
    else:
        print int(s[0:delIndex]+s[delIndex+1:len(s)])