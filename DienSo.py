t= int(input())
while t> 0:
    t-=1
    n= int(input())
    lst= []
    while True:
        arr= [int(i) for i in input().split()]
        lst.extend(arr)
        if(len(lst)==n): break
    s= set(lst)
    Max= max(s)
    Min= min(s)
    print(Max-Min+1-len(s))