N, K, L = [ int(x) for x in input().split() ]
#print("N, K, L:", N, K, L)
hom = [ int(x) for x in input().split() ]
#print("adatok: ", hom)
csucsok = [0]
meleg_napok_db = [0]
valasz = 0

for i in range(1,N-1):
    if hom[i] > hom[i-1] and hom[i] > hom[i+1]:
        meleg_napok_db.append(meleg_napok_db[-1]+1)
        csucsok.append(i+1)
    elif hom[i] < hom[i-1] and hom[i] < hom[i+1]:
        meleg_napok_db.append(meleg_napok_db[-1])
        csucsok.append(i+1)
csucsok.append(N+1)
meleg_napok_db.append(meleg_napok_db[-1])

#print("csucsok: ", csucsok)
#print("meleg napok db: ", meleg_napok_db)

i = 0
while i+K+L < len(csucsok)-1:
    if meleg_napok_db[i+K+L]-meleg_napok_db[i] == K:
        valasz += ((csucsok[i+1]-csucsok[i])*(csucsok[i+K+L+1]-csucsok[i+K+L]))
        #print(i, csucsok[i+1]-csucsok[i], csucsok[i+K+L+1]-csucsok[i+K+L])
    i += 1
print(valasz)

""" magyarazat
pl.:
N = 13; K = 2 (meleg napok); L = 1 (hideg napok)
sorszám: (0)  1  2  3  4  5  6  7  8  9  10  11  12  13  (14)
hőmérs : (-)  1  1  2  1  0  0  2  0  1   2   1   0   1  ( -)
csúcsok: (0)  -  -  M  -  -  -  M  H  -   M   -   H   -  (14)
melegdb: (0)        1           2  2      3       3      ( 3)

jó intervallumok:
[1, 8]; [2, 8]; [3, 8]; [1, 9]; [2, 9]; [3, 9]

[4, 10]; [5, 10]; [6, 10]; [7,1 0]; [4, 11]; [5, 11]; [6, 11]; [7, 11]

"""
