n=input()
res = "I hate"
for i in range(1,n):
    if i%2==0:
        res+=" that I hate"
    else:
        res+=" that I love"
print res+" it"