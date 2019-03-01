N, utak = [int(x) for x in input().split()]
lista = [int(x) for x in input().split()]

lista.sort(reverse = True)

ki = 0
while N > 0 and N-lista[0] > 0:
    N -= lista[0]
    ki += lista[0]-1
    lista.remove(lista[0])

ki += N-1

print(ki)
