
import math
def NgTo(n):
    if(n<2): return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0): return False
    return True
a = []
s1 = input().split()
n = int(s1[0])
m = int(s1[1])
for i in range(0,n):
    s2 = input().split()
    a.append(s2)
for i in range(0,n):
    for j in range(0,m):
        if NgTo(int(a[i][j])): print(1,end=" ")
        else: print(0, end=" ")
    print()