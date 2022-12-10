t= int(input())
while t>0:
    t-=1
    k= int(input())
    lst=[]
    while True:
        arr=[int(i) for i in input().split()]
        lst.extend(arr)
        if len(lst)==k: break
    lst.sort()
    d=dict()
    for i in lst:
        if(d.get(i)):
            d.update({i: d.get(i)+1})
        else:
            d.update({i: 1})
    out=[]
    for i in d.values():
        out.append(i)
    out.sort(reverse=True)
    for i in d:
        if(d.get(i)== out[0]):
            print(i)
            break
