t= int(input())
lst= []
while True:
    arr=[int(i) for i in input().split()]
    lst.extend(arr)
    if len(lst)==t: break
arr= []
chan= []
le=[]
for i in lst:
    if(i%2==0):
        chan.append(i)
        arr.append(0)
    else:
        le.append(i)
        arr.append(1)
chan.sort()
le.sort(reverse=True)
indexc=0
indexl=0
for i in arr:
    if(i==0):
        print(chan[indexc],end=" ")
        indexc+=1
    elif i==1 :
        print(le[indexl],end=' ')
        indexl+=1
