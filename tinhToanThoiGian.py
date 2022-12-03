class Player:
    def __init__(self,ma,ten,vao ,ra,gioChoi,phutChoi):
        self.ma = ma
        self.ten= ten
        self.vao = vao
        self.ra= ra
        self.gioChoi = gioChoi
        self.phutChoi= phutChoi
    def __str__(self):
        return '{} {} {} gio {} phut'.format(self.ma,self.ten, self.gioChoi,self.phutChoi)
class Time:
    def __init__(self,gio,phut):
        self.gio = gio
        self.phut= phut
t= int(input())
arr=[]
while t>0:
    t-=1
    ma= input()
    ten= input()
    vao= input().split(":")
    gioVao = Time(vao[0],vao[1])
    ra= input().split(":")
    gioRa= Time(ra[0],ra[1])
    gioChoi = int(gioRa.gio) - int(gioVao.gio)
    phutChoi=0
    if(int(gioRa.phut) < int(gioVao.phut)):
        gioChoi-=1
        phutChoi = -int(gioVao.phut)+ int(gioRa.phut)  +60
    else:
        phutChoi = int(gioRa.phut) - int(gioVao.phut)
    player= Player(ma, ten, vao, ra, gioChoi, phutChoi)
    arr.append(player)
arr.sort(key= lambda x:(-x.gioChoi,-x.phutChoi))
for i in arr:
    print(i.__str__())