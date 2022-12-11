x = input()
s= set()
arr=[]
for i in range(0,len(x),2):
    if(i+1<len(x)):
        k= str(x[i])+ str(x[i+1])
        s.add(k)
for i in s:
    arr.append(i)
arr.sort()
for i in arr:
    print(i,end=' ')