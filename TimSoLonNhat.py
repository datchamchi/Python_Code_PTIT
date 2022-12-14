t= int(input())
while t>0:
    t-=1
    x=input()
    out=[]
    s=''
    for i in x:
        if(i>='0' and i<='9'):
            s+= i
        else:
            if(len(s) >0): out.append(int(s))
            s=''
    if(len(s)>0): out.append(int(s))
    out.sort(reverse=True)
    print(out[0])

