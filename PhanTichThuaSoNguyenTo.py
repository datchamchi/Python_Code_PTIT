import math

t= int(input())
def phanTich(n):
    print('1  * ',end='')
    for i in range(2,int(math.sqrt(n)+1)):
        count=0
        while(n%i==0 and n>1):
            n=n/i
            count+=1
        if(count!=0) :
            print(str(i)+ '^'+str(count),end='')
            if(n>1): print(' * ',end='')
    if(n>1): print(str(int(n))+ "^1",end='')

while t>0:
    t-=1
    n=int(input())
    phanTich(n)
    print()