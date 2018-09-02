source="qwertyuiopasdfghjkl;zxcvbnm,./"
mark=raw_input()
n=1
if mark=="R":
    n=-1
s=""
for a in raw_input():
    index_=source.index(a)+n
    s+=source[index_]
print s