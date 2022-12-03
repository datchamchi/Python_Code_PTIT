lst=[]
arr = [int(x) for x in input().split()]
lst.extend(arr)
def check(a):
    for i in a:
        if(i!=0): return False
    return True
def checkTrung(a):
    n = a[0]
    for i in a:
        if(i!=n): return False
    return True
while(check(lst)== False):
    count=0
    while(checkTrung(lst)== False):
        count+=1
        for i in range(0,len(lst)-1):
            lst[i]=abs(lst[i]-lst[i+1])
        lst[3]= abs(lst[3]-)
    lst=[]
    while True:
        arr = [int(x) for x in input().split()]
        lst.extend(arr)
        if (len(lst) == 4): break;
