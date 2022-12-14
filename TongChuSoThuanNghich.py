t= int(input())
def check(s):
    if(len(s)<=1): return False
    for i in range(0,int(len(s)/2)):
        if(s[i] != s[len(s)-i-1]): return False
    return True
while t>0:
    t-=1
    s=input()
    sum=0
    for i in s:
        sum+= int(i)
    if(check(str(sum))): print('YES')
    else: print('NO')