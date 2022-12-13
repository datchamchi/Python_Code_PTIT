s= input()
lst=[]
for i in range(0,len(s),2):
    if(i+1<len(s)):
        k= str(s[i])+ str(s[i+1])
        lst.append(k)
d=dict()

for i in lst:
    if(d.get(i)):
        d.update({i:d.get(i)+1})
    else:
        d.update({i:1})
for  key,val in d.items():
    print(key,val)