from datetime import  datetime

class CaThi:
    def __init__(self,ngay,gio,phong):
        self.ngay= ngay
        self.gio= gio
        self.phong= phong
f= open('CATHI.in','r')
arr=[]
t= int(f.readline().strip())

while t>0:
    t-=1
    s= f.readline().strip()
    ngay=''
    if(len(s)!=0): ngay= s
    else: break
    gio = f.readline().strip()
    phong= f.readline().strip()
    cathi= CaThi(ngay,gio,phong)
    cathi.ngayChuan = datetime.strptime(cathi.ngay,'%d/%m/%Y')
    cathi.gioChuan = datetime.strptime(cathi.gio,'%H:%M')
    cathi.ma= 'C'+str(1001+len(arr))[1:]
    arr.append(cathi)
arr.sort(key= lambda x:(x.ngayChuan,x.gioChuan,x.ma))
for i in arr:
    print('{} {} {} {}'.format(i.ma,i.ngay,i.gio,i.phong))