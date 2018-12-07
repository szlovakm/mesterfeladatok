N, nev = input().split()
N = int(N)
jonev = []
for i in range(N):
    aktnev = input()
    if aktnev == nev:
        jonev.append(str(i+1))
print(len(jonev), " ".join(jonev))
