mgh = "aeiou"
szo = input().lower()
hossz = len(szo)
i = 0
db = 0
while i < hossz:
    if szo[i] not in mgh:
        db += 1
    else:
        if i > 0 and db > 0:
            print(db, end=' ')
            db = 0
    i += 1
if szo[-1] not in mgh:
    print(db)
