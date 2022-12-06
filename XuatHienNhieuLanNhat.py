t= int(input())
while t>0:
    t-=1
    n= int(input())
    lst=[]
    thisdict=dict({})
    while True:
        arr=[int(i) for i in input().split()]
        lst.extend(arr)
        if(len(lst)==n): break
    lst.sort()
    for i in arr:
        if(thisdict.get(i)):
            thisdict.update({i: thisdict.get(i)+1})
        else:
            thisdict.update({i:1})
    output=[]
    for i in thisdict.values():
        output.append(i)
    m = max(output)
    if(m>int(n/2)):
        for i in thisdict.keys():
            if(thisdict.get(i)==m):
                print(i)
                break
    else: print('NO')