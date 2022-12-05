t= int(input())
lst=[]
while t>0:
    t-=1
    a= input()
    s=""
    for i in a:
        if(i>='0' and i<='9'):
            s+= i
        else:
            if(len(s)!=0): lst.append(int(s))
            s=""
    if (len(s) != 0): lst.append(int(s))
lst.sort()
for i in lst:
    print(int(i))
