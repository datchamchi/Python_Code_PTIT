import math

t= int(input())
arr=[int(i) for i in input().split(' ')]
arr.sort()
def check(a,b):
    if(math.gcd(a,b)== 1): return True
    else: return False
for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        if(check(int(arr[i]),int(arr[j]))):
            print(str(arr[i])+ ' '+ str(arr[j]))

