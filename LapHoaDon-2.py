from datetime import  datetime
class KhachHang:
    def __init__(self,ten,phong,ngay,tien):
        self.ten= ten
        self.phong= phong
        self.ngay= ngay
        self.tien =tien
def convertDate(s):
    return datetime.strptime(s,'%d/%m/%Y')
t= int(input())
d={1:25,2:34,3:50,4:80}
arr=[]
while t>0:
    t-=1
    ten= input().strip()
    phong=input().strip()
    ngayNhan = convertDate(input().strip())
    ngayTra= convertDate(input().strip())
    tang= int(phong[0])
    dongia=d.get(tang)

    ngay = (ngayTra-ngayNhan).days +1

    tiendvu= int(input().strip())
    tien = (dongia) * ngay +tiendvu
    ma= 'KH'+ str(101+len(arr))[1::]
    kh = KhachHang(ten,phong,ngay,tien)
    kh.ma= ma
    kh.phong= phong
    arr.append(kh)
arr.sort(key=lambda x: (-x.tien))
for i in arr:
    print('{} {} {} {} {}'.format(i.ma,i.ten,i.phong,i.ngay,i.tien))