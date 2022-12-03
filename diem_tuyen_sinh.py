class ThiSinh:
    def __init__(self,ten,diem,dantoc,khuvuc):
        self.ten= ten
        self.diem= diem
        self.dantoc= dantoc
        self.khuvuc= khuvuc
        self.set_diem_cong()
        self.set_dan_toc()
        self.status = 'Do' if self.diem >=20.5 else 'Truot'
    def set_diem_cong(self):
        if(self.khuvuc== 1): self.diem +=1.5
        elif(self.khuvuc==2):self.diem +=1
    def set_dan_toc(self):
        if(self.dantoc!='Kinh'): self.diem +=1.5
        else: self.diem +=0
    def __str__(self):
        return self.ma +" "+ chuanhoa(self.ten)+ ' '+ '{:.1f}'.format(self.diem)+" "+self.status
def chuanhoa(x):
    return ('').join(x.strip().split('\\s+')).title()
t= int(input())
arr=[]
while t>0:
    t-=1
    ten= input()
    diem = float(input())
    dantoc= input()
    khuvuc= int(input())
    thisinh= ThiSinh(ten,diem,dantoc,khuvuc)
    arr.append(thisinh)
    thisinh.ma = 'TS' + str(len(arr)) if len(arr) >= 10 else 'TS0' + str(len(arr))


arr.sort(key= lambda p: (-p.diem,p.ma)  )

for ts in arr:
    print(ts.__str__())




