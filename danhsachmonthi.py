class Mon:
    def __init__(seklf,ma,ten,thi):
        self.ma = ma
        self.ten =ten
        self.thi = thi
    def __str__(self):
        return '{} {} {}'.format(self.ma,self.ten,self.thi)
t= int(input())
arr=[]
while t>0:
    t-=1
    ma= input()
    ten= input()
    thi = input()
    mon =Mon(ma, ten, thi)
    arr.append(mon)
arr.sort(key= lambda p: p.ma)
for i in arr:
    print(i.__str__())