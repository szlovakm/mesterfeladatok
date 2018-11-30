N = int(input())
lista = []
for i in range(N):
    lista.append(input())
honapok = [ 'januar', 'februar', 'marcius', \
            'aprilis', 'majus', 'junius', \
            'julius', 'augusztus', 'szeptember', \
            'oktober', 'november', 'december' ]
i = 0
while i < N and len(honapok) > 0:
    if lista[i] in honapok:
        honapok.remove(lista[i])
    i += 1
if len(honapok) > 0:
    print('NEM')
else:
    print('IGEN')
