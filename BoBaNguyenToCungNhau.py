import math

s= input().split()
a= int(s[0])
b= int(s[1])
def check(a,b):
    if(math.gcd(a,b)==1): return True
    else: return  False
for i in range(a,b-1):
    for j in range(i+1,b):
        if(check(i,j)):
            for k in range(j+1,b+1):
                if(check(j,k) and check(i,k)):
                    print('({}, {}, {})'.format(i,j,k))