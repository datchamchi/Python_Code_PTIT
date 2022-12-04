class Cuaro:
    def __init__(self,ten,diachi,tgian):
        self.ten = ten
        self.diachi = diachi
        self.tgian = tgian
        self.ma= maHoa(self.diachi) + maHoa(self.ten)
def maHoa(s):
    s= s.split()
    output=''
    for i in s:
        output+=i[0]
    return  output
def rounding(n):
    a= n*10
    if(a%10 >=5):
        a=a+1
    return a/10
listCr= []
t= int(input())

while t>0:
    t-=1
    ten = input()
    diachi = input()
    tgian = input().split(':')
    gio= int(tgian[0]) -6
    phut= int(tgian[1])/60
    cr= Cuaro(ten,diachi,gio+ phut)
    cr.tb= rounding(120/cr.tgian)
    listCr.append(cr)
listCr.sort(key= lambda x : (-x.tb))
for i in listCr:
    print('{} {} {} {:.0f} Km/h'.format(i.ma,i.ten,i.diachi,i.tb))