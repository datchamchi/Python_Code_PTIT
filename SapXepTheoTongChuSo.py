t= int(input())
def check(n):
    sum=0
    while n >=1:
        sum+= (n%10)
        n=int(n/10)
    return sum
while t>0:
    t-=1
    n=int(input())
    arr=[]
    while True:
        a=[int(i) for i in input().split()]
        arr.extend(a)
        if len(arr)== n: break
    d=dict()

    for i in arr:
        if(d.get(i)): continue
        else:
            d.update({i:check(i)})
    for i in sorted(d.items(),key=lambda x:(int(x[1]),int(x[0]))):
        print(i[0],end=' ')
    print()


