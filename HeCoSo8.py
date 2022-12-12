s= input()
output=''
def chuyen(s):
    sum=0
    for i in range(0,len(s)):
        if(s[i]=='1'):
            sum+= pow(2,len(s)-i-1)
    return sum
while(len(s) >= 3):
    x=s[-3:]
    output= str(chuyen(x)) + output
    s=s[:-3]
if(len(s) !=0):
    output= str(chuyen(s))+ output
print(output)

