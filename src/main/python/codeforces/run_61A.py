a=raw_input()
b=raw_input()
s=""
for i in range(len(a)):
    if a[i]==b[i]:
        s+='0'
    else:
        s+='1'
print s