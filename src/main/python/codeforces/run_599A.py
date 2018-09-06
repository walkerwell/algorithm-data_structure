d1,d2,d3=map(int,raw_input().split())
a=[]
minOne = min(d1,d2)
a.append(minOne*2+(d1+d2-minOne)*2)
a.append(d1+d2+d3)
minOne = min(d1,d2)
a.append(minOne*2+d3*2)
print min(a)