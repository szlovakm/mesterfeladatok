helysegek, fajok = [int(x) for x in input().split()]

tomb = []
for i in range(helysegek):
    tomb.append([int(x) for x in input().split()])

jok = []

for f in range(fajok):
    h = 0
    # ha találunk 0-t az oszlopban, akkor az már biztosan nem jó faj
    while h < helysegek and (tomb[h][f] != 0):
        h += 1
    # ha végigmentünk az oszlopon, és nem volt köztük 0, akkor jó faj
    if h >= helysegek:
        jok.append(str(f+1)) # a join miatt kell str-nek lennie

print(len(jok))
if len(jok) > 0:
    print(" ".join(jok))
