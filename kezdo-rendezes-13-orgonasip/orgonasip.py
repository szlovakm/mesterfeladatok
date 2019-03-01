N = int(input())
szamok = []
for i in range(N):
    szamok.append(int(input()))

# rendezzuk sorba, majd forditsuk meg!
szamok.sort()
szamok.reverse()

#kezdjuk a legnagyobbal
ki = [ str(szamok[0]) ] # stringkent tegyuk a listaba

# a paratlan indexueket szurjuk be az osszes
# eddigi ele;
# a paros indexueket tegyuk a lista vegere

for i in range(1,N):
    if i%2 == 1:
        ki.insert(0,str(szamok[i])) # stringkent tegyuk a listaba
    else:
        ki.append(str(szamok[i])) # stringkent tegyuk a listaba \
        # a join miatt

print(" ".join(ki))
    
