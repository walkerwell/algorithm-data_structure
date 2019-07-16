n=int(input())
s=input()
Anton=0
Danik=0
for i in range(n):
    if s[i]=='A':
        Anton+=1
    else:
        Danik+=1
if Anton>Danik:
    print ("Anton")
elif Anton<Danik:
    print ("Danik")
else:
    print ("Friendship")