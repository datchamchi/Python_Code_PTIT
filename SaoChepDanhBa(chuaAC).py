class User:
    def __init__(self,ngay,ten,sdt):
        self.ngay= ngay
        self.ten = ten
        self.sdt = sdt
        self.tenChuan= chuanHoTen(self.ten)

    def __str__(self):
        return self.ten+": "+self.sdt+" "+self.ngay
f= open('SOTAY.txt','r')
def chuanHoTen(s):
    arr=s.split()
    out=''
    for i in arr:
        out= i+out
    return out

lst =[]
ngay=""
while True:
    s= f.readline().strip()
    if(len(s)==0): break
    if(s.__contains__('Ngay')):
        tgian = (s.split())[-1]
        ngay= tgian
        ten = f.readline().strip()
        sdt= f.readline().strip()
        user= User(tgian,ten,sdt)
        lst.append(user)
    else:

        sdt= f.readline().strip()
        user= User(ngay,s,sdt)
        lst.append(user)
lst.sort(key=lambda x: (x.tenChuan))
output=""
for i in range(0,len(lst)):
    output+=lst[i].__str__()
    if(i!=len(lst)-1): output+="\n"
out = open('DIENTHOAI.txt','w')
out.write(output)

