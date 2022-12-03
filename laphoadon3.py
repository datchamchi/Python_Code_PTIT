class SanPham:
    def __init__(self,ma,ten,soluong,gia,chietkhau):
        self.ma= ma
        self.ten= ten
        self.soluong = soluong
        self.gia= gia
        self.chietkhau= chietkhau
        self.sum = self.soluong *self.gia - self.chietkhau
    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.ma,self.ten,self.soluong,self.gia,self.chietkhau,self.sum)
t= int(input())
arr=[]
while t>0:
    t-=1
    ma=input()
    ten=input()
    soluong= int(input())
    gia= int(input())
    chietkhau = int(input())
    arr.append(SanPham(ma, ten, soluong, gia, chietkhau))
arr.sort(key= lambda x: -x.sum)
for i in arr:
    print(i.__str__())