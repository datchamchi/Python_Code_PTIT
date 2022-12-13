import math
def check(n):
    if(n<2): return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0): return False
    return True
s= input().split()
n=int(s[0])
m= int(s[1])
matrix=[]
out=[]
ktra=1
for i in range(0,n):
    a=[int(i) for i in input().split()]
    for i in a:
        if(check(i)):
            ktra=0
            out.append(i)
    matrix.append(a)
if(ktra ==1):
    print('NOT FOUND')
else:
    gtMax= max(out)
    print(gtMax)
    for i in range(0,n):
        for j in range(0,m):
            if(matrix[i][j]== gtMax):
                print('Vi tri [{}][{}]'.format(i,j))
