class Allat:
    def __init__(self, regi, uj):
        self.regi = regi
        self.uj = uj
    # az alábbi tagfüggvények már csak a megjelenításhez kell,
    # a feladat megoldásához felesleges
    def __str__(self):
        return "{} -- {}".format(self.regi, self.uj)
    def __repr__(self):
        return self.__str__()


M, N = [ int(x) for x in input().split() ]

allatok = []
for i in range(N):
    r, u = [ int(x) for x in input().split() ]
    allatok.append(Allat(r, u))
#print(allatok)

# kinullázzuk a listát
elt = [ 0 for i in range(M+1) ]
# eggyel növeljük a megfelelő értéket, ha abban az évben
# élt az aktuális állat
for a in allatok:
    for i in range(a.uj, a.regi+1):
        elt[i] += 1
# m a lista (egyik) maximuma
m = max(elt)
print(m)
# visszafelé kell keresni az első ilyet a listában
print(M-elt[::-1].index(m))

