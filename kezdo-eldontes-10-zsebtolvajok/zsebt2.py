class Zsebtolvaj:
    def __init__(self, m, sz, h, l):
        self.mag = int(m)
        self.szem = sz
        self.haj = h
        self.le = int(l)

    def hasonlit(self, other):
        c = 0
        if self.mag == other.mag: c += 1
        if self.szem == other.szem: c += 1
        if self.haj == other.haj: c += 1
        if self.le == other.le: c += 1
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
        if zstl[i].hasonlit(zstl[j]): van = True
        j += 1
    i += 1

print("IGEN" if van else "NEM")
