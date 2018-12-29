M, N = [ int(x) for x in input().split() ]
bal = []
jobb = []
for i in range(N):
    b, j = [ -int(x) for x in input().split() ]
    bal.append(b)
    jobb.append(j)
bal.sort()
jobb.sort()

legtobb = 1
db = 1 # aktualisan elo allatok
mikor = bal[0]
i = 1
j = 0

while (i < N and j < N):
    if (bal[i] <= jobb[j]):
        db += 1
        if db > legtobb:
            legtobb = db
            mikor = bal[i]
        i += 1
    else:
        db -= 1
        j += 1

print(legtobb)
print(-mikor)

