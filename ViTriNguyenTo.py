import math

t= int(input())
arr= [2,3,5,7]
def checkNgTo(n):
    if(n<2): return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0): return False
    return True
def check(s):
    count=0
    for i in range (0,len(s)):
        if( checkNgTo(int(i)) and int(s[i])  in arr):
            count+=1
        if ( checkNgTo(int(i))==False and int(s[i]) not in arr):
            count+=1

    if(count==len(s)): return True
    else: return False

while t>0:
    t-=1
    s=input()
    if(check(s)): print('YES')
    else: print('NO')