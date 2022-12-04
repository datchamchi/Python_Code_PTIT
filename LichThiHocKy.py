from datetime import datetime
class Subject:
    def __init__(self,ma,ten):
        self.ma= ma
        self.ten = ten
class LichThi:
    def __init__(self,macathi,mamonhoc,tgian,ngay,gio,nhomthi):
        self.ngay=ngay
        self.gio = gio
        self.macathi= macathi
        self.mamonhoc= mamonhoc
        self.tgian=tgian
        self.nhomthi= nhomthi
def convertDate(s):
    return datetime.strptime(s,'%H:%M/%d/%m/%Y')
s= input().split()
listMH=[]
listLT=[]
n= int(s[0])
m= int(s[1])
while n>0:
    n-=1
    ma= input()
    ten= input()
    listMH.append(Subject(ma, ten))
while m>0:
    m-=1
    s= input().split()
    tgian = str(s[2]+"/"+ s[1])
    index= 'T'+ str(1001+ len(listLT))[1:]
    lichthi = LichThi(index,s[0],convertDate(tgian),s[1],s[2],(s[-1]))
    for i in listMH:
        if(i.ma == s[0]):
            lichthi.tenMon = i.ten
    listLT.append(lichthi)
listLT.sort(key= lambda x: (x.tgian,x.mamonhoc))
for i in listLT:
    print('{} {} {} {} {} {}'.format(i.macathi,i.mamonhoc,i.tenMon,i.ngay,i.gio,i.nhomthi))