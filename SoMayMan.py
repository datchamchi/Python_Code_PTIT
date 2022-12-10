def check(s):
    count=0
    for i in s:
        if(i=='4' or i=='7'):
            count+=1
    if(count ==4 or count ==7): return True
    else: return False
s=input()
if(check(s)): print('YES')
else: print('NO')