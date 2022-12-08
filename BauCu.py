s = input().split()
n = int(s[0])
k = int(s[1])
lst = []
d = dict()
while True:
    arr = [int(i) for i in input().split()]
    lst.extend(arr)
    if len(lst) == n : break
for i in lst:
    if(d.get(i)):
        d.update({i: d.get(i)+1})
    else:
        d.update({i:1})
xuatHien=[]
for i in d:
    xuatHien.append(d.get(i))
xuatHien.sort(reverse=True)
Max2=0
check=0
for i in range(1,len(xuatHien)):
    if(xuatHien[i] != xuatHien[0]):
        Max2= xuatHien[i]
        check=1
        break
if(check==0):
    print('NONE')
else:
    for i in d:
        if(d.get(i)==Max2):
            print(i)
            break