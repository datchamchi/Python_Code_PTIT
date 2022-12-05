import re
t= int(input())
thisdict = dict({})
def chuanHoa(k):
    s=''
    for i in k:
        if((i>='A' and i<='Z') or(i>='a' and i<='z')or(i>='0' and i<='9')):
            s+=i
        else : s+=" "
    return s
while t>0:
    t-=1
    x= chuanHoa(input().lower()).strip()
    s= re.split('\s+', x)
    for i in s:
        if(thisdict.get(i)):
            thisdict.update({i: thisdict.get(i)+1})
        else:
            thisdict.update({i:1})
res = {key: val for key, val in sorted(thisdict.items(), key = lambda ele: (-ele[1],ele[0]))}
for i in res:
    print(i,res.get(i))
