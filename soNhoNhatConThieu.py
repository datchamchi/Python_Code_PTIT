n= int(input())
arr=[]
s={}
while True:
    a =[int(i) for i in input().split()]
    arr.extend(a)
    if(len(arr)==n): break

arr.sort()
s= set(arr)
min= arr[0]
for i in s:
    if(min==i):
        min+=1
    else : break
print(min)

