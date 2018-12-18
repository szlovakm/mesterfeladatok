N, ar = [ int(x) for x in input().split() ]
ind = 0
leg = 10000 # 1 <= ar <= 10000
for i in range(N):
    uj = int(input())
    if uj > ar and uj < leg:
        ind = i
        leg = uj
if ind > 0:
    print(ind+1, leg)
else:
    print(-1)
