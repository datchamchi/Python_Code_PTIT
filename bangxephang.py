class SinhVien:
    def __init__(self,ten,ac,submit):
        self.ten= ten
        self.ac= ac
        self.submit =submit
    def __str__(self):
        return '{} {} {}'.format(self.ten,self.ac,self.submit)
t= int(input())
arr=[]
while t>0:
    t-=1
    ten= input()
    diem =input().split()
    ac= int(diem[0])
    submit = int(diem[1])
    sv= SinhVien(ten,ac,submit)
    arr.append(sv)
arr.sort(key= lambda p:(-p.ac,p.submit,p.ten))
for sv in arr:
    print(sv.__str__())