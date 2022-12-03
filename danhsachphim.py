class Phim:
    def __init__(self,ma,theloai,ngay,ten,tap):
        self.ma= ma
        self.ngay= ngay
        self.ten = ten
        self.tap = tap
        self.theloai= theloai
    def __str__(self):
        return '{} {} {} {} {}'.format(self.ma,self.theloai,self.ngay,self.ten,self.tap)
s= input().split()
n= int(s[0])
t= int(s[1])
tl=[]    # mang chua ten phim
arr=[]
def chuanhoaNgay(s):
    str= s.split('/')
    return str[2]+ str[1]+str[0]
for i in range(0,n):
    tl.append(input())
while t>0:
    t-=1
    ma= 'P'+str(1001+len(arr))[1:]
    theloai = tl[int(input()[2:])-1]
    ngay= input()
    ten = input()
    tap = int(input())
    phim= Phim(ma,theloai, ngay, ten, tap)
    phim.ngayChuan = chuanhoaNgay(phim.ngay)
    arr.append(phim)
arr.sort(key=lambda x: (x.ngayChuan,x.ten,-x.tap) )
for i in arr:
    print(i.__str__())
