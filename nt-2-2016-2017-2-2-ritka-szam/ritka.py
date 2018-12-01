def ritka(n):
    i = 0
    db = 1
    while db < n:
        i += 1
        if (i & 2*i) == 0:
            db += 1
    return i
print(ritka(int(input())))

