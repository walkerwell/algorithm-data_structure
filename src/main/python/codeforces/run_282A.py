res=0;
for i in range(input()):
    s=raw_input()
    if(s.find('+')<>-1):
        res += 1
    elif(s.find('-')<>-1):
        res -= 1
print res