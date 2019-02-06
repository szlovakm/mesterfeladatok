class Zsebtolvaj:
    def __init__(self, m, sz, h, l):
        self.mag = int(m)
        self.szem = sz
        self.haj = h
        self.le = int(l)

def egyezik(zs1, zs2):
    c = 0
    if zs1.mag == zs2.mag: c += 1
    if zs1.szem == zs2.szem: c += 1
    if zs1.haj == zs2. haj: c += 1
    if zs1.le == zs2.le: c += 1
    return (c >= 2)

n = int(input())
zstl = []
for i in range(n):
    m, sz, h, l = [x for x in input().split()]
    zstl.append(Zsebtolvaj(m, sz, h, l))

van = False
i = 0
while not van and i < n-1:
    j = i + 1
    while not van and j < n:
        if egyezik(zstl[i], zstl[j]): van = True
        j += 1
    i += 1

if van: print("IGEN")
else: print("NEM")

