t= int(input())
arr=[]
while t>0:
    t-=1
    s= input().split()
    output=''
    for i in s:
        if(len(output+i)<=100): output+= i
        if(len(output) <100): output+=" "
        else: break
    arr.append(output)
for i in arr:
    print(i)