N, M = [ int(i) for i in input().split() ]
szinek = [ "w" for i in range(N+1) ]
elek = [ [] for i in range(N+1) ]

for i in range(M):
    honnan, hova = [ int(i) for i in input().split() ]
    elek[honnan].append(hova)

#print(elek[1:])

"""
w = nem vizsgált (white)
g = éppen folyamatban van (grey)
b = befejeztük a vizsgálatát és a leszármazottaiét is (black)
"""

def vizsgal(p):
    #print(p, end=" ")
    #print(szinek[1:])
    global ciklusok, elagazasok
    if szinek[p] == "g":
        ciklusok += 1
    elif szinek[p] == "b":
        elagazasok += 1
    elif szinek[p] == "w":
        szinek[p] = "g"
        for i in elek[p]:
            vizsgal(i)
        szinek[p] = "b"

ciklusok=0
elagazasok=0

vizsgal(1)
#print()
print(ciklusok)
print(elagazasok)
