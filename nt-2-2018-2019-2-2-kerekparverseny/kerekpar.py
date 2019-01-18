N, M, K = [ int(i) for i in input().split() ]
varos = []
for i in range(N):
    varos.append([ int(i) for i in input().split() ])

def ut(x, y, hossz = 0, utvonal = ''):
    global maxhossz, jostart, start, joutvonal, holvoltmar
    if hossz > maxhossz:
        maxhossz = hossz
        jostart = start
        joutvonal = utvonal
        holvoltmar.append((x, y))
    if x < N-1:
        if abs(varos[x+1][y] - varos[x][y]) <= K:
            ut(x+1, y, hossz+1, utvonal+'L')
    if y < M-1:
        if abs(varos[x][y+1] - varos[x][y]) <= K:
            ut(x, y+1, hossz+1, utvonal+'J')

maxhossz = 0
holvoltmar = []

for i in range(N):
    for j in range(M):
        if not (i, j) in holvoltmar:
            start = (i, j)
            ut(i, j)

print(maxhossz)
print(str(jostart[0]+1)+' '+str(jostart[1]+1))
print(joutvonal)
