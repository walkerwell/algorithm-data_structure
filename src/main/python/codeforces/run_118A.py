s=raw_input().lower()
res=''
for i in range(len(s)):
    if s[i] not in ['A','a','O','o','Y','y','E','e','U','u','I','i']:
        res+='.'+s[i]
print(res)
