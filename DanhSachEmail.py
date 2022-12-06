f=open("CONTACT.in",'r')
output=set()

s=f.readline().lower().strip()
while(len(s)!=0):
    output.add(s)
    s=f.readline().lower().strip()
arr= []
for i in output:
    arr.append(i)
arr.sort()
for i in arr:
    print(i)
