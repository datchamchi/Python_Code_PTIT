a=[10,10,10,12,12,12,12,12,14,14,14,14,14,14,15]
b=[10,10,10,11,11,11,11,11,13,13,13,13,13,13,13]
c=[9,9,9,10,10,10,10,10,12,12,12,12,12,12,12]
d=[8,8,8,9,9,9,9,9,11,11,11,11,11,11,11]

for i in range(16):
    a.append(20)
    b.append(16)
    c.append(14)
    d.append(13)
class PhongBan:
    def __init__(self,ma,ten):
        self.ma = ma
        self.ten = ten
class NhanVien:
    def __init__(self,ma,tennv,luongcb,ngay):
        self.ma = ma
        self.tennv = tennv
        self.luongcb = luongcb
        self.ngay = ngay
        self.luong =self.tinh_luong()
    def tinh_luong(self):
        x= self.ma[0]
        y= int(self.ma[1:3]) -1
        hso=0
        if(x=='A'): hso = a[y]
        elif (x=='B'): hso= b[y]
        elif(x=='C'): hso =c[y]
        elif(x=='D'): hso =d[y]
        return hso*self.luongcb* self.ngay*1000
    def __str__(self):
        return '{} {} {} {:.0f}'.format(self.ma,self.tennv,self.tenpb,self.luong)
def tim_pb(x):
    for i in listPb:
        if(i.ma== x): return i.ten

n = int(input())
listPb = []
while n>0:
    n-=1
    str= input().split()
    pb =PhongBan(str[0],' '.join(str[1:]))
    listPb.append(pb)

t = int(input())
listNv=[]
while t>0:
    t-=1
    ma =input()
    tennv= input()
    luongcb = float(input())
    ngay = float(input())
    nv = NhanVien(ma, tennv, luongcb, ngay)
    nv.tenpb = tim_pb(nv.ma[3:])
    listNv.append(nv)
for i in listNv:
    print(i.__str__())