class HocSinh:
    def __init__(self,ten):
        self.ten= ten
t= int(input())
lst=[]
while t>0:
    t-=1
    ten = input()
    hs = HocSinh(ten)
    arr=[]
    while True:
        a= [float(i) for i in input().split()]
        arr.extend(a)
        if( len(arr)== 10): break
    tongdiem= 0
    for i in range(0,len(arr)):
        if(i==0 or i==1):
            tongdiem+= arr[i]*2
        else: tongdiem+= arr[i]
    tb = tongdiem/10/1.2
    status =''
    if(tb>=9): status='XUAT SAC'
    elif(tb>=8): status='GIOI'
    elif(tb>=7): status='KHA'
    elif(tb>=5): status='TB'
    else: status='YEU'
    hs.ma='HS' +str(101+len(lst))[1::]
    hs.tb= tb
    hs.status=status
    lst.append(hs)
lst.sort(key= lambda x:(-x.tb,x.ma))

for i in lst:
    print('{} {} {:.1f} {}'.format(i.ma,i.ten,i.tb,i.status))
