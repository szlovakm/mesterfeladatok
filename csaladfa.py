N = int(input())
fa = [ 0, 0 ]
for i in range(N-1):
    fa.append(int(input()))
#print(fa)

tav = [ 0 for i in range(N+1) ]
for i in range(N, 0, -1):
    x = i
    szint = 0
    while x != 1:
        x = fa[x]
        szint += 1
    tav[i] = szint
#print(tav)

leg = tav[0]
ind = []
for i,j in enumerate(tav):
    if j > leg:
        ind = []
        leg = j
        ind.append(i)
    elif j == leg:
        ind.append(i)
#print('leg: ', leg, 'indexek: ', ind)

print(len(ind), leg)
for i in ind:
    print(i, end=' ')
    
