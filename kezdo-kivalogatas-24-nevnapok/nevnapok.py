N, nev = input().split()
N = int(N)
nevek = []
jonev = []
for i in range(N):
    aktnev = input()
    nevek.append(aktnev)
    if aktnev == nev:
        jonev.append(str(i+1))
print(len(jonev), " ".join(jonev))
