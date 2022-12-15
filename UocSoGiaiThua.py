t= int(input())
while t>0:
    t-=1
    s= input().split()
    n= int(s[0])
    p = int(s[1])
    count=0
    while n>0:
        n //= p
        count+=n
    print(count)