t= int(input(

))
while t >0:
    t-=1
    s= input().split()
    n= int(s[0])
    k= int(s[1])
    lst=[]
    while True:
        arr= [int(i) for i in input().split()]
        lst.extend(arr)
        if(len(lst)==n): break
    output=[]
    m= max(lst)
    duong=[]
    for i in lst:
        if i<0:
            output.append(i)
        else: duong.append(i)
    output.extend(duong)
    for i in output:
        if(i== m):
            print(k,end=" ")
        print(i,end=" ")
    print()