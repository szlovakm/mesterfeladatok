N = int(input())
jegyek = []
elegtelenek = []
atlagok = []
for i in range(N):
    j = [ int(x) for x in input().split() ]
    jegyek.append(j)
    elegtelenek.append(j.count(1))
    atlagok.append(sum(j)/len(j))

i = 0
while i < N and elegtelenek[i] < 2:
    i += 1
if i >= N:
    i = 0
    while i < N and (atlagok[i]*10 % 10 < 4 or atlagok[i]*10 % 10 > 6):
        i += 1
    if i >= N:
        print(1)
    else:
        print(i+1)
else:
    print(i+1)

#print(jegyek)
#print(elegtelenek)
#print(atlagok)
