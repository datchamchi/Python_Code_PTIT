import math
import re
class SinhVien:
    def __init__(self,ten,diem1,diem2,diem3):
        self.ten= ten
        self.diem1= diem1
        self.diem2 =diem2
        self.diem3= diem3
        self.tong = self.diem1*3 + self.diem2*3 + self.diem3*2
        self.tb =float(self.tong/8)

    def __str__(self):
        return '{} {} {:.2f}'.format(self.ma, chuanhoa(self.ten),round_up(self.tb))
def chuanhoa(x):
    return (' ').join(re.split('\s+',x)).title()
def round_up(x):
    x=x*1000
    if(x%10 >=5): x=(int(x/10+1))*10
    else: x=int(x/10) *10
    return float(x/1000)
t = int(input())
arr=[]
def tim_xep_hang(n):
    for i in range (0,len(arr)):
        if(arr[i].tb == n): return i+1
while t>0:
    t-=1
    ten= input()
    diem1= float(input())
    diem2= float(input())
    diem3= float(input())
    sv= SinhVien(ten, diem1, diem2, diem3)
    sv.ma = 'SV' + str(len(arr)+1) if len(arr) >=10 else 'SV0' +str(len(arr)+1)
    arr.append(sv)
arr.sort(key=lambda p:(-p.tb,p.ma))

for sv in arr:
    print(sv.__str__() +" "+str(tim_xep_hang(sv.tb)) )

