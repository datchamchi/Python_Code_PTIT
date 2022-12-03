class Tram:
    def __init__(self,ma,ten,gio,phut,luongmua):
        self.ma= ma
        self.ten = ten
        self.gio= gio
        self.phut = phut
        self.luongmua= luongmua
class Time:
    def __int__(self,gio,phut):
        self.gio = gio
        self.phut= phut
arr=[]
# def check(name):
#     for i in arr:
#         if(i.ten == name): return True
#     return False
t= int(input())
while t>0:
    t-=1
    tentram = input()
    start= input().split(':')
    gioStart= int(start[0])
    phutStart= int(start[1])
    end= input().split(':')
    luongmua = int(input())
    gioEnd = int(end[0])
    phutEnd= int(end[1])
    gio = gioEnd- gioStart
    phut=0
    if(phutEnd < phutStart):
        gio-=1
        phut= phutEnd - phutStart +60
    else:
        phut= phutEnd - phutStart
    check=0
    for i in arr:
        if(i.ten == tentram ):
            check=1
            i.gio += gio
            i.phut += phut
            i.luongmua += luongmua
    if(check==0):
        tram = Tram('T'+ str(101+ len(arr))[1:],tentram,gio,phut,luongmua)
        arr.append(tram)
for i in arr:
    i.tb= float(i.luongmua/(i.gio + i.phut/60))
    print(i.ma +" "+ i.ten +" " +'{:.2f}'.format(i.tb))