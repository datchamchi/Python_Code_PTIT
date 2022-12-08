n = int(input())

matrix = []
for i in range(0,n):
    a=[int(i) for i in input().split()]
    matrix.append(a)
k=int(input())
tren=0
duoi=0
for i in range(0,n):
    for j in range(0,n):
        if(j<n-i-1 ): tren+=matrix[i][j]
        elif(j>n-i-1): duoi+= matrix[i][j]

if(abs(tren-duoi)<=k):
    print('YES')
    print(abs(tren-duoi))
else:
    print('NO')
    print(abs(tren - duoi))
