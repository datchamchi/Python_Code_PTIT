t= int(input())
count=0
ther=[]
while t>0:
    caudau= input().split()
    caucuoi = input().split()
    t-=2
    if(len(caudau)==6 and len(caucuoi)==8):
        ther.append(1)
        while(len(caudau)==6 and len(caucuoi) ==8 and t>0):
            caudau= input().split()
            caucuoi = input().split()
            t-=2
    if (len(caudau) == 7 and len(caucuoi) == 7):
        ther.append(2)
        caudau = input().split()
        caucuoi = input().split()
        t -= 2
print(len(ther))
for i in ther:
    print(i)