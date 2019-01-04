m,n=[int(x) for x in input().split()]

tomb=list()
for i in range(m):
    tomb.append([int(x) for x in input().split()])
    
vege=[ [1 for x in range(n)] for x in range(n) ]

for i in range(n):
    vege[i][i]=0

for i in range(m):
    for j in range(n):
        if tomb[i][j]>0:
            for k in range(n):
                if tomb[i][k]==0:
                    vege[j][k]=0

for i in range(n):
    print(sum(vege[i]), end=' ')
    if sum(vege[i])>0:
        for j in range(n):
            if vege[i][j]>0:
                print(j+1, end=' ')
    print()
