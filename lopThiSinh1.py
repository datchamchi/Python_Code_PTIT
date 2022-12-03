class ThiSinh:
    def __init__(self,ten,ngaysinh,diem1,diem2,diem3):
        self.ten = ten
        self.ngaysinh= ngaysinh
        self.diem1= diem1
        self.diem2= diem2
        self.diem3=diem3
        self.tong = self.diem1 +self.diem2+ self.diem3
    def __str__(self):
        return '{} {} {:.1f}'.format(self.ten,self.ngaysinh,self.tong)
ten= input()
ngaysinh= input()
diem1= float(input())
diem2=float(input())
diem3=float(input())
ts= ThiSinh(ten, ngaysinh, diem1, diem2, diem3)
print(ts.__str__())