import math


def check(n):
    if(n<2): return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0): return False
    return True
t= int(input())
lst=[]
while True:
    arr=[int(i) for i in input().split()]
    lst.extend(arr)
    if(len(lst)==t): break
d=dict()

for i in lst:
    if(check(i)):
        if(d.get(i)):
            d.update({i:d.get(i)+1})
        else:
            d.update({i:1})
for  key,val in d.items():
    print(key,val)