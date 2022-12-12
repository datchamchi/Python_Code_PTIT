from datetime import  datetime
class Ngay:
    def __init__(self,tgian,thu):
        self.tgian =tgian
        self.thu= thu
def convertDate(s):
    return datetime.strptime(s,'%d/%m/%Y')
t=int(input())
lst=[]
while t>0:
    t-=1
    s=input().split(' ')
    tgian =s[4]
    status= s[3]
    gia =0
    if(status =='IN'):
        if(s[1]=='Xe_con' and s[2]=='5'): gia=10000
        elif(s[1]=='Xe_con' and s[2]=='7'): gia=15000
        elif (s[1]=='Xe_tai' and s[2]=='2'): gia=20000
        elif(s[1]=='Xe_khach' and s[2]=='29'): gia=50000
        elif(s[1]=='Xe_khach' and s[2]=='45'): gia=70000
    check=1
    for i in lst:
        if(i.tgian ==tgian):
            check=0
            i.thu+= gia
    if(check==1):
        ngay= Ngay(tgian,gia)
        ngay.tgianChuan = convertDate(ngay.tgian)
        lst.append(ngay)
lst.sort(key=lambda x:(x.tgianChuan))
for i in lst:
    print('{}: {}'.format(i.tgian,i.thu))