from datetime import datetime
class Tram:
    def __init__(self,ten,tgian,luongmua):
        self.ten =ten
        self.tgian = tgian
        self.luongmua= luongmua
t= int(input())
lst=[]
while t>0:
    t-=1
    ten= input()
    start= datetime.strptime(input(),'%H:%M')
    end= datetime.strptime(input(),'%H:%M')
    tgian = end- start
    luongmua= int(input())
    check=0
    for i in lst:
        if(i.ten == ten):
            i.tgian += tgian
            i.luongmua += luongmua
            check=1
    if(check==0):
        tram = Tram(ten,tgian,luongmua)
        tram.ma= 'T'+str(101+ len(lst))[1:]
        lst.append(tram)
for i in lst:
    gio = i.tgian.seconds //3600
    phut= (i.tgian.seconds - gio *3600)/60
    i.tb = i.luongmua /(gio+ phut/60)
    print('{} {} {:.2f}'.format(i.ma, i.ten,i.tb))

