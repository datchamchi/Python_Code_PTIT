import re
t= int(input())
while t>0:
    t-=1
    s= input()
    ss= re.findall('[0-9]+', s)
    print(max([int(i) for i in ss]))