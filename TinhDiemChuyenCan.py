class SinhVien:
    def __init__(self,ma,ten,lop):
        self.ma =ma
        self.ten= ten
        self.lop= lop
class DiemDanh:
    def __init__(self,ma,diemdanh):
        self.ma= ma
        self.diemdanh= diemdanh
        self.comat= self.diemdanh.count('x')
        self.muon= self.diemdanh.count('m')
        self.vang = self.diemdanh.count('v')
        self.diem = 10-self.muon- self.vang*2

t= int(input())

n=t
listSv =[]
listDD =[]
while t>0:
    t-=1
    maSv = input()
    tenSv= input()
    lop = input()
    sv= SinhVien(maSv,tenSv,lop)
    listSv.append(sv)
while n>0:
    n-=1
    s= input().split()
    diemdanh= DiemDanh(s[0],s[1])
    listDD.append(diemdanh)
for sv in listSv:
    for i in listDD:
        if(sv.ma == i.ma):
            print(sv.ma+" "+ sv.ten+" "+ sv.lop +' '+ str(i.diem if i.diem >=0 else 0) +" " + ('KDDK' if (i.diem<=0) else ''))