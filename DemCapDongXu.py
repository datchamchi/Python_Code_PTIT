n= int(input())
matrix =[]
ans=0
while True:
    s=input()
    hang = s.count('C')
    ans+= hang*(hang-1) //2
    matrix.append(s)
    if(len(matrix)==n): break

for i in range(0,n):
    cot=0
    for j in range(0,n):
        if(matrix[j][i]=='C'):
            cot+=1
    ans += cot* (cot-1) //2
print(ans)





