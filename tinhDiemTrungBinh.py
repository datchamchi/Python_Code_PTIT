n= int(input())
lst=[]
while True:
    arr= [float(i) for i in input().split()]
    lst.extend(arr)
    if(len(lst) ==n): break
lst.sort()
min=lst[0]
max =lst[-1]
sum=0
count=0
for i in lst:
    if(i!= min and i!=max):
        sum+=i
        count+=1

print('{:.2f}'.format(sum/count))